import json
import os
from functools import wraps
from logging import Logger
from threading import Thread
from time import sleep
from typing import Any, Callable, Dict, Optional, Union

import pika
from pika.exceptions import AMQPError

from apps import LOGGER


def retry_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Method to reconnect
    """

    @wraps(func)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        for attempt in range(1, 11):
            try:
                return func(self, *args, **kwargs)
            except AMQPError as exc:
                try:
                    self.disconnect()
                except Exception as dis_exc:
                    LOGGER.debug(
                        "Rabbit disconnect error: %s", str(dis_exc), exc_info=True
                    )
                LOGGER.exception(exc)
                LOGGER.error(f"Try attempt {attempt}")
                self.connect()
                continue

    return wrapper


class Rabbit:
    def __init__(
        self,
        config_dir="." + os.sep,
        config_file="rabbit.yaml",
        log: Optional[Logger] = None,
        section="rabbit",
        heartbeat=0,
    ):
        """
        For config loader lab lib
        :param config_dir:
        :param config_file:
        :param log:
        :param section:
        :param heartbeat:
        """
        config = dict()  # type: Dict[str, Any]
        self._host = config["rabbit_host"]
        self._port = config["rabbit_port"]
        self._vhost = config["rabbit_vhost"]
        self._user = config["rabbit_user"]
        self._password = config["rabbit_password"]
        self.job_handler = self.default_job_handler
        self._heartbeat = heartbeat
        self.log = log

    def default_job_handler(self, ch: Any, me: Any, pr: Any, bo: Any):
        self.log.info("Received and no processed message: %s", bo)

    def connect(self) -> None:
        """
        method connect to rabbit
        """
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                self._host,
                self._port,
                self._vhost,
                pika.PlainCredentials(self._user, self._password),
                heartbeat=58,  # max limit 60 sec on prod rabbit
                tcp_options=dict(TCP_KEEPIDLE=60 * 5),
            )
        )
        self.channel = self.connection.channel()

    @retry_decorator
    def consume_jobs(
        self,
        topic: str = "",
        exchange="",
        function_handler=None,
        auto_ack: bool = False,
    ) -> None:
        """
        Base consumer
        """
        # self.channel.basic_qos(prefetch_count=1)

        self.job_handler = function_handler

        queue_name = f"{exchange}.{topic}" if exchange else topic
        self.channel.basic_consume(
            queue=queue_name,
            on_message_callback=self.job_handler_wrapper,
            auto_ack=auto_ack,  # because if lost connect in run service the task is restarted
        )
        self.channel.start_consuming()

    def job_handler_wrapper(self, ch: Any, me: Any, pr: Any, bo: Any) -> None:
        """
        code from a digital core
        """
        try:
            job = Thread(target=self.job_handler, args=(ch, me, pr, bo))
            job.start()
            while job.is_alive():
                self.connection.process_data_events(time_limit=0)
                sleep(0.1)
        except Exception as e:
            self.log.exception(
                f"Exception {e} while handling new job message: " + bo.decode()
            )
        ch.basic_ack(delivery_tag=me.delivery_tag)

    @retry_decorator
    def send_msg(
        self,
        topic="dummy",
        msg: Union[Dict, str] = None,
        headers: Dict = None,
        exchange="",
    ):
        """
        base sender
        """
        if isinstance(msg, dict):
            msg = json.dumps(msg)
        u_msg = msg
        # prop = {"delivery_mode": 2}
        prop = dict()
        if headers:
            prop["headers"] = headers
        self.channel.basic_publish(
            exchange=exchange,
            routing_key=topic,
            body=u_msg,
            properties=pika.BasicProperties(**prop),
        )

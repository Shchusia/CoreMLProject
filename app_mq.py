"""
Service runner
"""
# pylint: disable=broad-except,protected-access
import time
from traceback import format_exc

from apps import CONFIG, LOGGER
from mq_rabbit.service_handler import ServiceHandler
from utils import Rabbit


def runner_service() -> None:
    """
    Main method
    """
    service = ServiceHandler(log=LOGGER)
    LOGGER.debug("%s init service", CONFIG.SERVICE_NAME)

    rbt = Rabbit(heartbeat=58, log=LOGGER)

    LOGGER.debug(
        "%s started listen exchange: `%s` topic `%s`",
        CONFIG.SERVICE_NAME,
        CONFIG.INPUT_EXCHANGE,
        CONFIG.INPUT_TOPIC,
    )

    rbt.consume_jobs(
        topic=CONFIG.INPUT_TOPIC,
        exchange=CONFIG.INPUT_EXCHANGE,
        function_handler=service.service_handler,
        auto_ack=False,
    )


if __name__ == "__main__":
    while True:
        try:
            LOGGER.info("Started %s", CONFIG.SERVICE_NAME)
            runner_service()
        except KeyboardInterrupt:
            break
        except Exception as e:
            LOGGER.exception("Exception: %s, Traceback: %s", e, format_exc())
        time.sleep(CONFIG.SECONDS_BETWEEN_RECONNECT)
        LOGGER.info("Finished %s", CONFIG.SERVICE_NAME)

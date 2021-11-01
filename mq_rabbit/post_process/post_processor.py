from typing import Any, Optional

from orchestrator_service import CommandHandlerPostStrategy

from apps import CONFIG
from mq_rabbit.utils import MessageQueue
from utils import Rabbit


class ResponseSender(CommandHandlerPostStrategy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._rabbit = Rabbit()

    def post_process(
        self, msg: MessageQueue, additional_data: Optional[Any] = None
    ) -> None:
        # make or response
        msg.update_body(additional_data)
        response = msg.get_body()
        header = msg.get_header(returned_type_str=False)

        self._rabbit.send_msg(
            topic=CONFIG.OUTPUT_TOPIC,
            msg=response,
            headers=header,
            exchange=CONFIG.OUTPUT_EXCHANGE,
        )

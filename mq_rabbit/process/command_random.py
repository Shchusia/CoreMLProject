from typing import Any, Optional, Tuple

from orchestrator_service import CommandHandlerStrategy

from apps import DICT_MODELS
from mq_rabbit.utils import MessageQueue


class CommandRandom(CommandHandlerStrategy):
    target_command = "random_predict"

    def process(self, msg: MessageQueue) -> Tuple[MessageQueue, Optional[Any]]:
        # other logic
        result_predict = DICT_MODELS["random"].predict()
        return msg, result_predict

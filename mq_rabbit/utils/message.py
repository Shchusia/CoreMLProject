import json
from typing import Any, Dict, Tuple, Union

from orchestrator_service import Message
from pydantic import BaseModel, ValidationError


class QueueMsgStructure(BaseModel):
    job_type: str
    # some fields


class MessageQueue(Message):
    """
    Class message for processing in service
    """

    def __init__(self, _ch, _deliver, _properties, body: Union[str, bytes]):
        converted_body: Dict[str, Any] = json.loads(body)
        try:
            header = dict(_properties.headers)  # type: dict
        except Exception:
            header = dict()
        super().__init__(body=converted_body, header=header)

        self.header["command"] = self.body.get("job_type", None)

    def is_valid_msg(self) -> Tuple[bool, Union[Exception, None]]:
        """
        method check is valid current received message
        :return:
        """
        try:
            QueueMsgStructure(**self.body)
            return True, None
        except ValidationError as exc:
            return False, exc
        except Exception as exc:
            return False, exc

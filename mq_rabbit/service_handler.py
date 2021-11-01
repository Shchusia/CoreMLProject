from orchestrator_service import Service, ServiceBlock, ServiceBuilder

from apps import CONFIG

from .post_process import ResponseSender
from .process import CommandLgbm, CommandRandom
from .utils import MessageQueue


class ServiceHandler(Service):
    _default_command = ""
    service_commands = ServiceBuilder(
        ServiceBlock(CommandLgbm, ResponseSender),
        ServiceBlock(CommandRandom),
        default_post_process=ResponseSender,
    )

    def service_handler(self, *args):
        msg = MessageQueue(*args)

        self.logger.info("%s got job (%s)", CONFIG.SERVICE_NAME, msg.get_body())
        is_valid, exc = msg.is_valid_msg()
        if not is_valid:
            self.logger.error(
                "%s: invalid message structure: `%s`. Error(s) %s",
                CONFIG.SERVICE_NAME,
                msg.get_body(),
                str(exc),
            )
            return None
        self.handle(msg)

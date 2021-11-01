import os
from logging import Logger

# from graylogger import init_graylogger
from werkzeug import import_string

from utils import init_models

DICT_MODELS = init_models()
# logger = init_graylogger()

path_to_config = os.getenv("APP_SETTINGS", "config.Config")
CONFIG = import_string(path_to_config)
LOGGER = Logger(CONFIG.SERVICE_NAME)

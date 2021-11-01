import os
from pathlib import Path
from uuid import uuid4

BASE_DIR = Path(os.path.dirname(os.path.realpath(__file__))).parent


class Config:
    """
    Base class for configs class
    """

    SERVICE_NAME = "DSCore"
    DEBUG = False
    SECRET_KEY = str(uuid4())
    API_VERSION = "0.0.1"

    # REST
    BASE_URL = "/core"
    BASE_DIR = BASE_DIR
    IS_PRINT_ERROR_IN_MSG = False
    PROMETHEUS_INIT_VERSION = 1

    # MQ
    INPUT_TOPIC = os.environ.get("INPUT_TOPIC", "predict")
    INPUT_EXCHANGE = os.environ.get("INPUT_EXCHANGE", "")
    OUTPUT_TOPIC = os.environ.get("OUTPUT_TOPIC", "predicted")
    OUTPUT_EXCHANGE = os.environ.get("OUTPUT_EXCHANGE", "")
    SECONDS_BETWEEN_RECONNECT = 60  # sec


class DevConfig(Config):
    """
    Override for dev env
    """

    DEBUG = True
    SERVICE_NAME = "DSCoreDev"
    SECRET_KEY = "secret_dev"
    IS_PRINT_ERROR_IN_MSG = True


class TestConfig(Config):
    """
    Override for test|pilot env
    """

    SERVICE_NAME = "DSCoreTest"
    SECRET_KEY = "secret_test"
    IS_PRINT_ERROR_IN_MSG = True


class ProdConfig(Config):
    """
    Override for prod env
    """

    pass

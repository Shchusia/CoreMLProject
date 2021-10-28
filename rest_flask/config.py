import os
from pathlib import Path
from uuid import uuid4

BASE_DIR = Path(os.path.dirname(os.path.realpath(__file__))).parent


class Config:
    """
    Base class for configs class
    """

    APP_NAME = "DSCore"
    DEBUG = False
    SECRET_KEY = str(uuid4())
    API_VERSION = "0.0.1"

    BASE_URL = "/core"
    BASE_DIR = BASE_DIR
    IS_PRINT_ERROR_IN_MSG = False
    PROMETHEUS_INIT_VERSION = 1


class DevConfig(Config):
    """
    Override for dev env
    """

    DEBUG = True
    APP_NAME = "DSCoreDev"
    SECRET_KEY = "secret_dev"
    IS_PRINT_ERROR_IN_MSG = True


class TestConfig(Config):
    """
    Override for test|pilot env
    """

    APP_NAME = "DSCoreTest"
    SECRET_KEY = "secret_test"
    IS_PRINT_ERROR_IN_MSG = True


class ProdConfig(Config):
    """
    Override for prod env
    """

    pass

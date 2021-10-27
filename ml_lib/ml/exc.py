"""
Module with exceptions ML global
"""
from .lgbm_model.exc import *  # noqa
from .random_forest_model.exc import *  # noqa


class MLException(Exception):
    """
    class for base exceptions
    """

    pass


class ModelNotFoundException(Exception):
    """
    Exception if model not found in time execution method `load`
    """

    pass

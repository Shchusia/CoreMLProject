"""
Module with config and constants
"""
from .ml.lgbm_model.utils.metrics import WMAPE
from .pre_processing import (
    add_synthetic_feature1,
    add_synthetic_feature2,
    add_synthetic_feature3,
)


class MLConfig:  # pylint: disable=too-few-public-methods
    """
    A class for storing basic models settings
        and other necessary constants
    """

    # ######################
    # ### global configs ###
    # ######################
    DATE_TIME_ORIGIN_FORMAT = "%Y-%m-%d %H:%M:%S"

    # ##################
    # ### LGB config ###
    # ##################
    LGBM_FEATURES_TO_APPLY = [add_synthetic_feature1, add_synthetic_feature2]
    LGBM_DEFAULT_METRICS = WMAPE

    # #################
    # ### RF config ###
    # #################
    RF_FEATURES_TO_APPLY = [add_synthetic_feature3, add_synthetic_feature2]

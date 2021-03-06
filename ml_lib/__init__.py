"""
Ml lib module with functions for models
"""
from typing import Tuple

from .config import MLConfig
from .ml.lgbm_model.lgbm import LGBM
from .ml.ml_model import MLModel
from .ml.random_forest_model.random_forest import RandomForest

__version__ = "0.0.1"

__all__: Tuple[str, ...] = (
    "MLConfig",
    "MLModel",
    # optional objects maybe not import in future
    # "get_object_config"
    "LGBM",
    "RandomForest",
)

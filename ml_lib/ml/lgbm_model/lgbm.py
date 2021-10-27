"""
Module with example class for lgbm model
"""
# pylint: disable=invalid-name
import pickle
from logging import Logger
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import lightgbm as lgb
import pandas as pd

from ml_lib.config import MLConfig
from ml_lib.ml.ml_model import MLModel
from ml_lib.utils import get_object_config

from .utils.metrics import make_feval

default_logger = Logger(__name__)


class LGBM(MLModel):
    """
    Model LGBM for example
    """

    model_type = "example_lgb"

    __model: lgb.Booster = None
    __fit_params: Dict[str, Any]
    __model_details: Dict[str, Any]

    def __init__(
        self,
        path_to_model: Optional[Union[Path, str]] = None,
        logger: Optional[Logger] = None,
        config: Optional[MLConfig] = None,
    ):
        """
        Init lgbm adapter class
        :param Optional[Path] path_to_model:
        :param Optional[Logger] logger: for logging information
        :param Optional[MLConfig] config: settings class which will use some static constants
        """
        self.__config = get_object_config(config)
        self.__logger = logger
        self.__fit_params, self.__model_details = dict(), dict()

        if path_to_model:
            self.load(path_to_model)

    def _apply_features(self, base_df: pd.DataFrame) -> pd.DataFrame:
        df = base_df
        for feature_generator in self.__config.LGBM_FEATURES_TO_APPLY:
            df = feature_generator(df)
        return df

    def fit(  # type: ignore
        self,
        df_x: pd.DataFrame,
        df_y: pd.Series,
        valid_sets: List[Tuple[pd.DataFrame, pd.Series]] = None,
        feval: Optional[Callable] = None,
        *args: List[Any],
        **kwargs: Dict[str, Any]
    ) -> None:
        """
        Method to fit lgb model
        :param pd.DataFrame df_x:
        :param pd.Series df_y:
        :param feval:  custom evaluation function
            if needed - (pred, pred_y) -> (name, score, higher_is_better)
            check out metrics.make_feval function to turn your metric in feval func
        :param valid_sets: list of valid sets in format
            [(valid1_X, valid1_Y), (valid2_X, valid2_Y), ...]
        :param args:
        :param kwargs:
        :return:
        """

        df_x = self._apply_features(df_x)
        dataset = lgb.Dataset(data=df_x, label=df_y)
        if not feval:
            feval = make_feval(self.__config.LGBM_DEFAULT_METRICS)
        valid_sets = (
            [lgb.Dataset(X, Y) for X, Y in valid_sets]
            if valid_sets is not None
            else None
        )
        self.__logger.info("Started train LGBM model")
        self.__model = lgb.train(
            params=self.__fit_params,
            train_set=dataset,
            valid_sets=valid_sets,
            feval=feval,
        )
        self.__model_details["WAPE"] = self.__model.best_score["valid_0"]
        self.__logger.info("Finished train LGBM model")

    def predict(self, data_to_predictions: pd.DataFrame, *args, **kwargs) -> pd.Series:  # type: ignore
        """

        :param data_to_predictions:
        :param args:
        :param kwargs:
        :return:
        """
        self.__logger.info("Started LGBM model predict")
        result = self.__model.predict(data_to_predictions)
        self.__logger.info("Finished LGBM model predict")
        return result

    def save(self, path_to_model: Union[Path, str], *args, **kwargs) -> None:  # type: ignore
        self.__logger.info("start saving LGBM models...")

        with open(path_to_model, "wb") as file:
            pickle.dump(
                obj={
                    "models": self.__model,
                    "fit_params": self.__fit_params,
                    "model_details": self.__model_details,
                },
                file=file,
            )
        self.__logger.info("models LGBM saved.")

    def load(self, path_to_model: Union[Path, str]) -> None:  # type: ignore
        self.__logger.info("loading LGBM models...")
        with open(path_to_model, "rb") as file:
            obj = pickle.load(file)
            self.__model = obj["models"]
            self.__fit_params = obj.get("fit_params", dict())
            self.__model_details = obj.get("model_details", dict())
        self.__logger.info("models LGBM load.")

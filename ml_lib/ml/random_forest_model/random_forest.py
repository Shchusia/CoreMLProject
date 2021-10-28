"""
Module with example class for random forest model
"""
# pylint: disable=invalid-name
import pickle
from logging import Logger
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from ml_lib.config import MLConfig
from ml_lib.ml.ml_model import MLModel
from ml_lib.utils import get_object_config

DEFAULT_LOGGER = Logger(__name__)


class RandomForest(MLModel):
    """
    Model RandomForestClassifier for example
    """

    model_type = "example_random_forest"

    __model: RandomForestClassifier
    __fit_params: Dict[str, Any]
    __model_details: Dict[str, Any]

    def __init__(
        self,
        path_to_model: Optional[Union[Path, str]] = None,
        logger: Optional[Logger] = None,
        config: Optional[MLConfig] = None,
    ):
        """
        Init RandomForestClassifier adapter class
        :param Optional[Path] path_to_model:
        :param Optional[Logger] logger: for logging information
        :param Optional[MLConfig] config: settings class which will use some static constants
        """
        self.__config = get_object_config(config)
        self.__logger = logger or DEFAULT_LOGGER

        self.__fit_params, self.__model_details = dict(), dict()

        if path_to_model:
            self.load(path_to_model)

    def _apply_features(self, base_df: pd.DataFrame) -> pd.DataFrame:
        df = base_df
        for feature_generator in self.__config.RF_FEATURES_TO_APPLY:
            df = feature_generator(df)
        return df

    def fit(  # type: ignore
        self,
        df_x: pd.DataFrame,
        df_y: pd.Series,
        *args: List[Any],
        **kwargs: Dict[str, Any]
    ) -> None:
        """
        Method to fit RandomForestClassifier model
        :param pd.DataFrame df_x:
        :param pd.Series df_y:
        :param args:
        :param kwargs:
        :return:
        """

        df_x = self._apply_features(df_x)
        self.__logger.info("Started train RandomForestClassifier model")
        self.__model = RandomForestClassifier().fit(df_x, df_y)
        self.__logger.info("Finished train RandomForestClassifier model")

    def predict(  # type: ignore
        self, data_to_predictions: pd.DataFrame, *args, **kwargs
    ) -> pd.Series:
        """

        :param data_to_predictions:
        :param args:
        :param kwargs:
        :return:
        """
        self.__logger.info("Started RandomForestClassifier model predict")
        result = self.__model.predict(data_to_predictions)
        self.__logger.info("Finished RandomForestClassifier model predict")
        return result

    def save(self, path_to_model: Union[Path, str], *args, **kwargs) -> None:  # type: ignore
        self.__logger.info("start saving RandomForestClassifier models...")

        with open(path_to_model, "wb") as file:
            pickle.dump(
                obj={
                    "models": self.__model,
                    "fit_params": self.__fit_params,
                    "model_details": self.__model_details,
                },
                file=file,
            )
        self.__logger.info("models RandomForestClassifier saved.")

    def load(self, path_to_model: Union[Path, str]) -> None:  # type: ignore
        self.__logger.info("loading RandomForestClassifier models...")
        with open(path_to_model, "rb") as file:
            obj = pickle.load(file)
            self.__model = obj["models"]
            self.__fit_params = obj.get("fit_params", dict())
            self.__model_details = obj.get("model_details", dict())
        self.__logger.info("models RandomForestClassifier load.")

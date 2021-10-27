"""
Module with abstract class for ML Models
"""
from abc import ABC, abstractmethod
from typing import Any, Dict


class MLModel(ABC):
    """
    Base class for ML Models
    """

    __model_details: Dict
    __fit_params: Dict

    @property
    def model_type(self):
        """
        Property for naming models
        """
        raise NotImplementedError

    @abstractmethod
    def fit(self, *args, **kwargs):
        """
        Method fit model
        """
        raise NotImplementedError

    @abstractmethod
    def predict(self, *args, **kwargs) -> Any:
        """
        Method predict result by inputted value
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def save(self, *args, **kwargs) -> None:
        """
        save model to storage
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def load(self, *args, **kwargs) -> None:
        """
        load model from storage
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError

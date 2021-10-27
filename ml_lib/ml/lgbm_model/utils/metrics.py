"""
Module for metrics
X stands for predicted values
Y stands for true values
"""
# pylint: disable=invalid-name
from typing import Callable

import numpy as np
from lightgbm.basic import Dataset


def MAE(X: np.ndarray, Y: np.ndarray):
    """ Mean absolute error """
    return np.mean(np.absolute(Y - X))


def MAPE(X: np.ndarray, Y: np.ndarray):
    """ Mean absolute percentage error """
    return np.mean(np.absolute((Y - X) / Y))


def RMSE(X: np.ndarray, Y: np.ndarray):
    """ Root mean squared error """
    return np.sqrt(((Y - X) ** 2).mean())


def MSE(X: np.ndarray, Y: np.ndarray):
    """ Mean squared error """
    return ((Y - X) ** 2).mean()


def WMAPE(X: np.ndarray, Y: np.ndarray):
    """ Weighted mean absolute percentage error """
    return np.sum(np.absolute(Y - X)) / np.sum(np.absolute(Y))


def sMAPE(X: np.ndarray, Y: np.ndarray):
    """ Symmetric mean absolute percentage error """
    return np.mean(2 * np.absolute(X - Y) / (np.absolute(X) + np.absolute(Y)))


def make_feval(f: Callable, name: str = None, higher_better: bool = False) -> Callable:
    """
    Function factory to transform @f to @feval required by LightGBM
    :
        f: function of 2 arguments (predictions, true_values) -> score
        name: name of function (f.__name__ will be used if None)
        higher_better: True if higher score is better, otherwise False
    Returns:
        feval: function of 2 arguments
            (predictions, Dataset with true labels) -> (name, score, higher_better)
    """

    def feval(X: np.ndarray, Y: Dataset):
        return (
            name if name is not None else f.__name__,
            f(X, Y.get_label()),
            higher_better,
        )

    return feval

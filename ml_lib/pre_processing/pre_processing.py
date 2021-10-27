"""
Module contains functions for data preprocessing before training
"""
# pylint: disable=invalid-name
import pandas as pd


def change_raw_data(df: pd.DataFrame, *args, **kwargs) -> pd.DataFrame:
    """
    Function to modify or extend raw data
    :param pd.DataFrame df: data to modify
    :return: changed pd.DataFrame df
    """
    return df

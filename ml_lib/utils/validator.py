"""
module with validation functions
"""
from typing import Optional, Type, Union

from ml_lib import MLConfig


def get_object_config(obj: Optional[Union[object, Type[MLConfig]]] = None) -> MLConfig:
    """
    Function to get config for work models
    :param Optional[Union[object, Type[MLConfig]]] obj:object to check
    :return: default  if obj is none or incorrect type
    """
    return_obj = MLConfig()
    if obj:
        if callable(obj) and issubclass(obj, MLConfig):  # type: ignore
            return_obj = obj()
        elif isinstance(obj, MLConfig):
            return_obj = obj
    return return_obj

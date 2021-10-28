"""
the module contains functions for working with data extraction or formation
"""
from logging import Logger
from typing import Any, Dict, Optional

import pandas as pd

from .db_handler import DBHandler

DEFAULT_LOGGER = Logger(__name__)


class DataHandler:
    """
    class for extracting data
    """

    _db_handler: DBHandler

    def __init__(self, logger: Optional[Logger] = None):
        self._config_procedures = {}  # type: Dict[str, Any]  # load from config
        self._db_config = {}  # type: Dict[str, Any]  # load from config
        self._db_handler = DBHandler(logger=logger)
        self.__logger = logger or DEFAULT_LOGGER

    def get_data_for_predictions(self, *args, **kwargs) -> Optional[pd.DataFrame]:
        """
        Function for extract data
        :param args: possible parameters for forming a request to the procedure
        :param kwargs:
        :return:
        """
        procedure = self._config_procedures["procedure_extract_data_for_predictions"]
        return self._db_handler.get_data_from_db(procedure)

    def get_data_for_fit(self, *args, **kwargs) -> Optional[pd.DataFrame]:
        """
        Function for extract data
        :param args: possible parameters for forming a request to the procedure
        :param kwargs:
        :return:
        """
        procedure = self._config_procedures["procedure_extract_data_for_fit"]
        return self._db_handler.get_data_from_db(procedure)

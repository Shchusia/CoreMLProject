"""
Module with a class for working with a database as a data source
"""
# pylint: disable=invalid-name
from logging import Logger
from typing import Any, Dict, Optional

import bcpy
import numpy as np
import pandas as pd
from pyodbc import Connection
from sqlalchemy.engine import Engine

from .exc import ColumnsForInsertNotFound, CrashDBSessionException

DEFAULT_LOGGER = Logger(__name__)


class DBHandler:
    """
    class for handling work source data.
    """

    __connection: Connection = None
    __engine: Engine = None

    def __init__(
        self,
        logger: Optional[Logger] = None,
        # maybe_configs #
    ):
        # create connection
        # create engine
        self.__autocommit_engine = self.__engine.execution_options(
            isolation_level="AUTOCOMMIT"
        )

        self._db_config = dict()  # type: Dict[str, Any]
        self.__logger = logger or DEFAULT_LOGGER

    @staticmethod
    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i : i + n]

    def bcp_bulk_insert(self, df: pd.DataFrame, schema_name: str, table_name: str):
        sql_config = {
            "server": self._db_config["host"],
            "database": self._db_config["dbname"],
        }
        output_columns = self.get_columns_from_table(schema_name, table_name)
        self.__logger.debug("missing columns in dataframe to write:")
        self.__logger.debug(list(set(output_columns) - set(df.columns)))
        for col in list(set(output_columns) - set(df.columns)):
            df[col] = np.NaN
        df = df[output_columns]
        bdf = bcpy.DataFrame(df)
        batch_size = 10000  # maximum number of rows in batch
        sql_table = bcpy.SqlTable(sql_config, schema_name=schema_name, table=table_name)
        try:
            bdf.to_sql(sql_table, use_existing_sql_table=True, batch_size=batch_size)
        except Exception as exc:
            self.__logger.error(
                "bcp bulk insert crashed during insert data into %s, Error: %s",
                table_name,
                str(exc),
                exc_info=True,
            )
            raise CrashDBSessionException(
                f"bcp bulk insert crashed " f"during insert data into {table_name}"
            )

    def get_columns_from_table(
        self, schema_name: str, table_name: str
    ) -> Optional[pd.Index]:
        """

        :param schema_name:
        :param table_name:
        :return:
        """
        query = f"""
            SELECT name as column_name
            FROM sys.columns c
            WHERE object_id = OBJECT_ID('{schema_name}.{table_name}')
        """
        try:
            output_columns = pd.read_sql_query(query, self.__autocommit_engine)
            return output_columns.column_name
        except FileNotFoundError:
            raise ColumnsForInsertNotFound(table_name)

    def _read_with_query(self, query: str) -> Optional[pd.DataFrame]:
        try:
            self.__logger.debug("start with procedure")
            df = pd.read_sql_query(
                query, self.__autocommit_engine, parse_dates=["date", "predictionDate"]
            )
            self.__logger.debug("sql query done")
        except Exception as exc:
            self.__logger.error("SQL query crashed: %s", str(exc), exc_info=True)
            df = None
        return df

    def get_data_from_db(
        self, procedure: str, *args, **kwargs
    ) -> Optional[pd.DataFrame]:
        """
        Function execute
        :param procedure:
        :param args:
        :param kwargs:
        :return:
        """
        query = "SET NOCOUNT ON; EXEC " + procedure
        return self._read_with_query(query)

    def write_data_to_db(
        self, df: pd.DataFrame, schema_name: str, table_name: str, *args, **kwargs
    ):
        """
        Function write to db
        :param pd.DataFrame df:
        :param str schema_name:
        :param str table_name:
        :param args:
        :param kwargs:
        :return:
        """
        self.__logger.debug(f"start load to database {len(df)} rows...")
        self.bcp_bulk_insert(df, schema_name, table_name)
        self.__logger.debug("predictions loaded to database")

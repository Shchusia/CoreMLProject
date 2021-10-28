"""
Module with exceptions data_handler
"""


class DataHandlerException(Exception):
    """
    Base exception for DataHandler Module
    """

    pass


class CrashDBSessionException(DataHandlerException):
    """
    Error in time execution query.
    """

    def __init__(self, message: str):
        self.message = message
        Exception.__init__(self, self.message)


class ColumnsForInsertNotFound(Exception):
    def __init__(self, table_name: str):
        self.message = f"Can't extract columns for insert into table {table_name}"
        Exception.__init__(self, self.message)

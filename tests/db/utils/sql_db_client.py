"""
This module is written to handle SQL database related operations
"""
import pyodbc
import pandas as pd
from common.utils.exceptions import LogInFailed, QueryExecutionFailed
from common.utils.shared_utils import logging_service

log = logging_service.getLogger(__file__)

# pylint: disable=c-extension-no-member


class AzureSQLDatabase:
    """
    A class to interact with an Azure SQL Database.

    """

    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None

    def establish_connection(self):
        """
        Establishes a connection to the Azure SQL Database.
        """
        try:
            self.connection = pyodbc.connect(self.connection_string)
            log.info("Logged in Successfully")

        except pyodbc.Error as e:
            log.error(f"Error while connecting to the database: {e}")
            raise LogInFailed("Log in failed") from e

    def close_connection(self):
        """
        Closes the connection to the Azure SQL Database.
        """
        if self.connection:
            self.connection.close()
            log.info("Connection closed")

    def execute_query(self, query):
        """
        Executes a given SQL query.

        Parameters
        ----------
        query : str
            The SQL query to be executed.

        Returns
        -------
        None
        """
        log.info(f"Query: {query}")
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            cursor.commit()

        except pyodbc.Error as e:
            log.error(f"Encountered error while executing query {e}")
            raise QueryExecutionFailed("Encountered error while executing query") from e

    def fetch_all(self, query):
        """
        Fetches all rows from a query result.

        Parameters
        ----------
        query : str
            The SQL query to fetch results from.

        Returns
        -------
        list
            A list of rows from the query result.
        """
        log.info(f"Query: {query}")
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()

        except pyodbc.Error as e:
            log.error(f"Encountered error while executing query {e}")
            raise QueryExecutionFailed("Encountered error while executing query") from e

    def to_dataframe(self, query):
        """
        Converts query results to a pandas DataFrame.

        Parameters
        ----------
        query : str
            The SQL query to fetch results from.

        Returns
        -------
        DataFrame
            A pandas DataFrame containing the query results.
        """
        log.info(f"Query: {query}")
        try:
            df = pd.read_sql(query, self.connection)
            return df
        except pyodbc.Error as e:
            log.error(f"Encountered error while executing query {e}")
            raise QueryExecutionFailed("Encountered error while executing query") from e

    def get_row_count(self, query):
        """
        Gets the row count for a given query.

        Parameters
        ----------
        query : str
            The SQL query to count rows from.

        Returns
        -------
        int
            The row count of the query result.
        """
        log.info(f"Query: {query}")
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.rowcount

        except pyodbc.Error as e:
            log.error(f"Encountered error while executing query {e}")
            raise QueryExecutionFailed("Encountered error while executing query") from e

    def list_tables(self):
        """
        Fetches the list of all tables in the database.

        Returns
        -------
        list
            A list of table names in the database.
        """
        query = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';"
        log.info(f"Query: {query}")
        try:
            return self.fetch_all(query)

        except pyodbc.Error as e:
            log.error(f"Encountered error while executing query {e}")
            raise QueryExecutionFailed("Encountered error while executing query") from e

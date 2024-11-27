"""
DB related util is written in this module
"""
# pylint: disable=too-few-public-methods
# pylint: disable=raise-missing-from


class DBUtils:
    """
    Initialize this class to make use static methods which are useful for db operations
    """

    @staticmethod
    def read_sql_qry(filepath):
        """
        Read database query, useful for .sql format
        :param filepath:
        """
        with open(filepath, "r", encoding='utf-8') as file:
            _query = file.read()

        return _query

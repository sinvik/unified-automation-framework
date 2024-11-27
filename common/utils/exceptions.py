"""
exceptions.py is built to handle Errors and logging
"""


class APIFailureError(Exception):
    """
    Handle API call
    """


class LogInFailed(Exception):
    """Handle logins"""


class QueryExecutionFailed(Exception):
    """Db related operations"""


class SomeErrorOuccured(Exception):
    """When want to include in multiple steps"""

from behave.runner import Context
from common.utils.environment_variable import get_env_variable
from common.utils.file_and_folder_service import FileFolderService
from tests.db.utils.sql_db_client import AzureSQLDatabase
from common.utils.shared_utils import AllureUtils, in_memory_log


def before_all(context):
    """
    Initialize logger
    """
    username = get_env_variable("sql_user")
    password = get_env_variable("sql_pwd")

    file_folder_service = FileFolderService()
    config = file_folder_service.load_config()["DB"]

    driver = config["driver"]
    server = config["server"]
    database = config["db_name"]

    connection_string = (f"Driver={str(driver)};"
                         f"Server={server};"
                         f"Database={database};"
                         f"Uid={username};"
                         f"Pwd={password};"
                         f"Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

    context.db = AzureSQLDatabase(connection_string)


def before_scenario(context: Context, scenario):
    """
    Setup steps to be executed before each scenario.
    """
    in_memory_log.clear()


def after_scenario(context: Context, scenario):
    """
    Cleanup steps to be executed after each scenario.
    """

    collected_logs = in_memory_log.get_logs()
    AllureUtils.attach_log_to_allure(collected_logs, "log")


def after_all(context):
    context.db.close_connection()

"""
This module is helpful for loading data to SQL database
"""
# pylint: disable=unused-import
import setup_path
from tests.db.utils.sql_db_client import AzureSQLDatabase
from tests.db.utils.db_utils import DBUtils
from common.utils.environment_variable import get_env_variable
from common.utils.file_and_folder_service import FileFolderService
from common.utils.shared_utils import logging_service, in_memory_log
from common.utils.exceptions import SomeErrorOuccured


if __name__ == "__main__":

    file_folder_service = FileFolderService()
    file_folder_service.delete_and_create_folder(file_folder_service.logs)
    log_file = f"{file_folder_service.logs}/drop_and_load.log"

    log = logging_service.getLogger(__file__)

    username = get_env_variable("sql_user")
    password = get_env_variable("sql_pwd")

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

    drop_tables_qry = DBUtils.read_sql_qry(
        f"{file_folder_service.data_load_queries}/drop_tables.sql"
    )

    create_table_qry = DBUtils.read_sql_qry(
        f"{file_folder_service.data_load_queries}/create_table.sql"
    )

    load_data_qry = DBUtils.read_sql_qry(f"{file_folder_service.data_load_queries}/load_data.sql")

    try:
        db = AzureSQLDatabase(connection_string)
        db.establish_connection()

        db.execute_query(drop_tables_qry)
        db.execute_query(create_table_qry)
        db.execute_query(load_data_qry)

        collected_logs = in_memory_log.get_logs()
        file_folder_service.write_text(log_file, collected_logs)

    except SomeErrorOuccured as e:
        log.error(f"Some error occurred while loading data to SQL. {e}")
        collected_logs = in_memory_log.get_logs()
        file_folder_service.write_text(log_file, collected_logs)
        raise SomeErrorOuccured("Some error occurred while loading data to SQL.") from e

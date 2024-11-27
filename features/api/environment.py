from behave.runner import Context
from common.utils.file_and_folder_service import FileFolderService
from common.utils.shared_utils import AllureUtils, in_memory_log


def before_all(context: Context):
    """
    Initialize logger
    """
    config = FileFolderService().load_config()
    context.base_url = config["API"]["base_url"]


def before_scenario(context: Context, scenario):
    """
    Setup steps to be executed before each scenario.
    """
    in_memory_log.clear()


def after_scenario(context: Context, scenario):
    """
    Setup steps to be executed before each scenario.
    """

    collected_logs = in_memory_log.get_logs()
    AllureUtils.attach_log_to_allure(collected_logs, "log")

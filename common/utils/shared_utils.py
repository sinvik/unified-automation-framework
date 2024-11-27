"""
This module contain logging services for allure/ BDD framework
"""
import logging
import allure


class InMemoryLogHandler(logging.Handler):
    """
    Since after each scenario the log should be cleared and
    should not save logs for passing scenario
    """

    def __init__(self):
        super().__init__()
        self.logs = []

    def emit(self, record):
        """
         Append logs
        """
        self.logs.append(self.format(record))

    def get_logs(self):
        """
        Get log content
        """

        return "\n".join(self.logs)

    def clear(self):
        """
        Clear previous logs
        """

        self.logs = []


# pylint: disable=too-few-public-methods
class AllureUtils:
    """
    Useful allure utils
    """
    @staticmethod
    def attach_log_to_allure(content, name):
        """
        On failure attach log of whole scenario
        :param content:
        :param name:
        """

        allure.attach(str(content), name=name,
                      attachment_type=allure.attachment_type.TEXT)


FORMAT = '%(asctime)s %(filename)s %(levelname)s: %(message)s'
logging.basicConfig(format=FORMAT)
in_memory_log = InMemoryLogHandler()
in_memory_log.setFormatter(logging.Formatter(FORMAT))
logging.getLogger().addHandler(in_memory_log)
logging_service = logging

"""
This module contain utilities for file and folder related operations
"""

import json
import os
import shutil


class FileFolderService:
    """
    Requisites:
        - config dir
        - reports dir
        - logs dir
    """
    def __init__(self):
        cwd = os.getcwd()
        self.config_path = f'{cwd}/common/config/config.json'
        self.reports = f'{cwd}/reports'
        self.logs = f'{cwd}/logs'
        self.data_load_queries = f'{cwd}/tests/db/data_load'

    def load_config(self):
        """
        Read config file
        """
        with open(self.config_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def delete_and_create_folder(abs_folder_path):
        """
        Delete and create folder
        :params abs_folder_path: complete path for the folder
        """
        if os.path.isdir(abs_folder_path):
            shutil.rmtree(abs_folder_path)

        os.makedirs(abs_folder_path)

    @staticmethod
    def write_text(file_path, content):
        """
        Write text file
        """
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

"""
Useful methods to load environment variable from .env file
"""

import os
from dotenv import load_dotenv


def load_environment():
    """
    Load the environment variables from the .env file.
    """
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    if os.path.exists(env_path):
        load_dotenv(dotenv_path=env_path)
    else:
        raise FileNotFoundError(f".env file not found at {env_path}")


def get_env_variable(key, default=None):
    """
    Get an environment variable value, with an optional default.
    """
    return os.getenv(key, default)

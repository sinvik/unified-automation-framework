"""
This module is written to handle json content
"""


class APIUtils:
    """
    APIUtils facilitates utilities to deal with json content
    """
    @staticmethod
    def parse_json(response):
        """
        Parse the JSON content from a response object.

        :param response: Response object from an API request.
        :return: Parsed JSON data as a dictionary.
        :raises: ValueError if the response content is not valid JSON.
        """
        return response.json()

    @staticmethod
    def validate_json_structure(json_data, expected_keys):
        """
        Validate that a JSON object contains the expected keys.

        :param json_data: JSON data as a dictionary.
        :param expected_keys: List of keys that are expected to be in the JSON data.
        :return: True if all expected keys are present, False otherwise.
        """
        return all(key in json_data for key in expected_keys)

    @staticmethod
    def print_response_details(response):
        """
        Print the details of an API response.

        :param response: Response object from an API request.
        """
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")

    @staticmethod
    def is_status_code(response, expected_status):
        """
        Check if the response status code matches the expected status code.

        :param response: Response object from an API request.
        :param expected_status: Expected HTTP status code.
        :return: True if the status code matches, False otherwise.
        """
        return response.status_code == expected_status

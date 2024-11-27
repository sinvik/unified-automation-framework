"""
A service class to handle HTTP operations such as GET, POST, PUT, and DELETE
using the Python 'requests' library."""
from typing import Any, Dict, Optional, Union
import requests
from common.utils.shared_utils import AllureUtils, logging_service
from common.utils.exceptions import APIFailureError

log = logging_service.getLogger(__file__)


class APIService:
    """
    A service class to handle HTTP operations such as GET, POST, PUT, and DELETE
    using the Python 'requests' library.
    """

    def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None,
                 params: Optional[Dict[str, Any]] = None):
        """
        Initializes the APIService with a base URL, optional headers, and optional parameters.

        Args:
            base_url (str): The base URL for the API.
            headers (Optional[Dict[str, str]]): Optional headers to include in the requests.
            params (Optional[Dict[str, Any]]): Optional parameters to include in the requests.
        """
        self.base_url = base_url
        self.headers = headers or {}
        self.params = params or {}

    def get_request(self, endpoint: str, **kwargs) -> Union[Dict[str, Any], str]:
        """
        Sends a GET request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the GET request to.
            **kwargs: Additional arguments passed to requests.get().

        Returns:
            Union[Dict[str, Any], str]: The response JSON data or an error message.
        """
        url = f"{self.base_url}/{endpoint}"
        log.info(f"Get request {url}")

        response_data = None
        try:
            response = requests.get(url, headers=self.headers, params=self.params,
                                    timeout=5, **kwargs)

            if response.ok:
                log.info(f"Status code {response.status_code}")
            else:
                log.error(f"Status code {response.status_code}")

            response.raise_for_status()
            response_data = response.json()
            AllureUtils.attach_log_to_allure(response_data, "get_request_log")

            return response_data

        except requests.exceptions.RequestException as e:
            log.error(f"Get request failure {e}")
            AllureUtils.attach_log_to_allure(response_data, "get_request_log")
            raise APIFailureError("API request failed") from e

    def post_request(self, endpoint: str, data: Optional[Dict[str, Any]] = None,
                     json: Optional[Dict[str, Any]] = None, **kwargs) -> Union[Dict[str, Any], str]:
        """
        Sends a POST request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the POST request to.
            data (Optional[Dict[str, Any]]): The form data to send in the body of the request.
            json (Optional[Dict[str, Any]]): The JSON data to send in the body of the request.
            **kwargs: Additional arguments passed to requests.post().

        Returns:
            Union[Dict[str, Any], str]: The response JSON data or an error message.
        """
        url = f"{self.base_url}/{endpoint}"
        log.info(f"Post request {url}")

        response_data = None
        try:
            response = requests.post(url, headers=self.headers,
                                     params=self.params, data=data, json=json,
                                     timeout=5, **kwargs)

            if response.ok:
                log.info(f"Status code {response.status_code}")
            else:
                log.error(f"Status code {response.status_code}")

            response.raise_for_status()

            response_data = response.json()
            AllureUtils.attach_log_to_allure(response_data, "post_request_log")
            return response_data

        except requests.exceptions.RequestException as e:
            log.error(f"Post request failure {e}")
            AllureUtils.attach_log_to_allure(response_data, "post_request_log")
            raise APIFailureError("API request failed") from e

    def put_request(self, endpoint: str, data: Optional[Dict[str, Any]] = None,
                    json: Optional[Dict[str, Any]] = None, **kwargs) -> Union[Dict[str, Any], str]:
        """
        Sends a PUT request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the PUT request to.
            data (Optional[Dict[str, Any]]): The form data to send in the body of the request.
            json (Optional[Dict[str, Any]]): The JSON data to send in the body of the request.
            **kwargs: Additional arguments passed to requests.put().

        Returns:
            Union[Dict[str, Any], str]: The response JSON data or an error message.
        """
        url = f"{self.base_url}/{endpoint}"
        log.info(f"Put request {url}")

        response_data = None
        try:
            response = requests.put(url, headers=self.headers,
                                    params=self.params, data=data, json=json,
                                    timeout=5, **kwargs)

            if response.ok:
                log.info(f"Status code {response.status_code}")
            else:
                log.error(f"Status code {response.status_code}")

            response.raise_for_status()

            response_data = response.json()
            AllureUtils.attach_log_to_allure(response_data, "put_request_log")
            return response_data

        except requests.exceptions.RequestException as e:
            log.error(f"Put request failure {e}")
            AllureUtils.attach_log_to_allure(response_data, "put_request_log")
            raise APIFailureError("API request failed") from e

    def delete_request(self, endpoint: str, **kwargs) -> Union[Dict[str, Any], str]:
        """
        Sends a DELETE request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the DELETE request to.
            **kwargs: Additional arguments passed to requests.delete().

        Returns:
            Union[Dict[str, Any], str]: The response JSON data or an error message.
        """
        url = f"{self.base_url}/{endpoint}"
        log.info(f"Delete request {url}")

        response_data = None
        try:
            response = requests.delete(url, headers=self.headers, params=self.params,
                                       timeout=5, **kwargs)

            if response.ok:
                log.info(f"Status code {response.status_code}")
            else:
                log.error(f"Status code {response.status_code}")
                raise APIFailureError("API error")

            response.raise_for_status()

            response_data = response.json()
            AllureUtils.attach_log_to_allure(response_data, "delete_request_log")
            return response_data

        except requests.exceptions.RequestException as e:
            log.error(f"Delete request failure {e}")
            AllureUtils.attach_log_to_allure(response_data, "delete_request_log")
            raise APIFailureError("API request failed") from e

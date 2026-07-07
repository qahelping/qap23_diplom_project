import requests

from core.logger import logger
from test_data.urls import BASE_URL


class HttpClient:
    @staticmethod
    def build_url(endpoint: str):
        return f"https://{BASE_URL}/public/v2/{endpoint.lstrip('/')}"

    def _request(self, method: str, endpoint: str, data: str | None = None, headers: str | None = None):
        self._logger_request(method=method, endpoint=self.build_url(endpoint), data=data, headers=headers)

        response = requests.request(method=method, url=self.build_url(endpoint), data=data, headers=headers)

        self._logger_response(method=method, endpoint=self.build_url(endpoint), response=response)

        response_dict = response.json()
        return response_dict, response.status_code

    def get(self, endpoint: str):
        return self._request("GET", endpoint)

    @staticmethod
    def _logger_request(method: str, endpoint: str, data: str | None = None, headers: str | None = None):
        logger.info("[API REQUEST] %s %s", method, endpoint)
        if data:
            logger.info("[API REQUEST DATA] %s", data)
        if headers:
            logger.info("[API REQUEST HEADERS] %s", headers)

    @staticmethod
    def _logger_response(method: str, endpoint: str, response: requests.Response):
        logger.info("[API RESPONSE] %s %s %s", method, endpoint, response.status_code)
        logger.info("[API RESPONSE DATA] %s", response.text)

import allure

from core.http_client import HttpClient
from core.logger import logger
from models.user_models import User, UsersResponse


class UserService(HttpClient):
    def __init__(self):
        self.url = "/users"

    @allure.step("Get list of user")
    def get_list_of_user(self):
        response, status_code = self.get(self.url)
        logger.info("[USER SERVICE, GET LIST USER] %s", response)
        return UsersResponse(users=response), status_code

    @allure.step("Get user by id: {user_id}")
    def get_user_by_id(self, user_id):
        response = self.get(f"{self.url}/{user_id}")
        return User(**response)

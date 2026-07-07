import json

import allure
import pytest
import requests

from core.get_env import GORES_TOKEN
from models.user_models import UsersResponse
from services.user_service import UserService
from test_data.get_random_body import get_random_user
from test_data.users_list import USERS_LIST, get_user_by_id


@allure.suite("API")
@allure.feature("User")
class TestUser:
    @pytest.mark.user_1
    @allure.title("Get user")
    def test_get_user(self):
        user_service = UserService()

        response, status_code = user_service.get_list_of_user()
        assert status_code == 200  # noqa: PLR2004
        assert response == UsersResponse(users=USERS_LIST)

    @allure.title("Get user by id")
    def test_get_user_by_id(self):
        user_service = UserService()
        user_id = "8512085"

        response = user_service.get_user_by_id(user_id)

        assert response.status_code == 200  # noqa: PLR2004
        assert response == get_user_by_id(user_id)

    @allure.title("Create user")
    def test_create_user(self):
        headers = {
            "Authorization": f"Bearer {GORES_TOKEN}",
            "Accept": "application/json",
            "Content-type": "application/json",
        }

        url = "https://gorest.co.in/public/v2/users"

        body = get_random_user()
        response = requests.post(url, headers=headers, data=json.dumps(body))
        response_json = response.json()
        assert response.status_code == 201  # noqa: PLR2004
        assert response_json["name"] == body["name"]
        assert response_json["email"] == body["email"]
        assert response_json["gender"] == body["gender"]
        assert response_json["status"] == body["status"]

        user_id = response_json["id"]
        url = f"https://gorest.co.in/public/v2/users/{user_id}"
        response = requests.get(url, headers=headers)

        response_json = response.json()
        assert response.status_code == 200  # noqa: PLR2004

        assert response_json["name"] == body["name"]
        assert response_json["email"] == body["email"]
        assert response_json["gender"] == body["gender"]
        assert response_json["status"] == body["status"]

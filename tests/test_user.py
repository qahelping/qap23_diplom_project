import json

import requests

from core.get_env import GORES_TOKEN
from test_data.get_random_body import get_random_user
from test_data.users_list import USERS_LIST, get_user_by_id


def test_get_user():
    url = "https://gorest.co.in/public/v2/users"
    response = requests.get(url)

    response_json = response.json()
    assert response.status_code == 200  # noqa: PLR2004
    assert response_json == USERS_LIST


def test_get_user_by_id():
    user_id = "8512085"
    url = f"https://gorest.co.in/public/v2/users/{user_id}"
    response = requests.get(url)

    response_json = response.json()
    assert response.status_code == 200  # noqa: PLR2004
    assert response_json == get_user_by_id(user_id)


def test_create_user():
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

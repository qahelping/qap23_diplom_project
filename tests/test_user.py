import requests

from test_data.users_list import USERS_LIST, get_user_by_id


def test_get_user():
    url = 'https://gorest.co.in/public/v2/users'
    response = requests.get(url)

    response_json = response.json()
    assert response.status_code == 200
    assert response_json == USERS_LIST


def test_get_user_by_id():
    user_id = '8512085'
    url = f'https://gorest.co.in/public/v2/users/{user_id}'
    response = requests.get(url)

    response_json = response.json()
    assert response.status_code == 200
    assert response_json == get_user_by_id(user_id)



def test_create_user():
    url = 'https://gorest.co.in/public/v2/users'
    response = requests.post(url)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json
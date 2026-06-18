from core.http_client import prepare_header
from test_data.get_random_body import get_random_user


def test_get_headers():
    data = prepare_header("token")

    assert data == {
        "Authorization": "Bearer token",
        "Accept": "application/json",
        "Content-type": "application/json",
    }


def test_get_random_user():
    data = get_random_user()

    assert data["name"]
    assert data["email"]
    assert data["gender"]
    assert data["status"] == "active"

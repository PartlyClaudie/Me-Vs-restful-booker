import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com"

@pytest.fixture(scope="session")
def auth_token():
    response = requests.post(
        f"{BASE_URL}/auth",
        json={"username": "admin", "password": "password123"}
    )
    return response.json()["token"]
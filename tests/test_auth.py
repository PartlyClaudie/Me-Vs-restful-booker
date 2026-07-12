import requests

BASE_URL = "https://restful-booker.herokuapp.com"

def test_create_token_with_valid_credentials():
    response = requests.post(
        f"{BASE_URL}/auth",
        json={"username": "admin", "password": "password123"}
    )
    assert response.status_code == 200
    assert "token" in response.json()

def test_create_token_with_invalid_credentials():
    response = requests.post(
        f"{BASE_URL}/auth",
        json={"username": "wrong", "password": "wrong"}
    )
    assert response.status_code == 200  # this API returns 200 even on failure — worth noting!
    assert "token" not in response.json()
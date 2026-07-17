import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def auth_token(base_url):
    response = requests.post(
        f"{base_url}/auth",
        json={"username": "admin", "password": "password123"}
    )
    return response.json()["token"]


@pytest.fixture
def booking_payload():
    return {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "Breakfast"
    }


@pytest.fixture
def created_booking(base_url, booking_payload):
    response = requests.post(f"{base_url}/booking", json=booking_payload)
    return response.json()
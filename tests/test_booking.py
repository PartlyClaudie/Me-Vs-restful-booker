import requests

BASE_URL = "https://restful-booker.herokuapp.com"

def sample_booking():
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

def test_create_booking():
    response = requests.post(f"{BASE_URL}/booking", json=sample_booking())
    assert response.status_code == 200
    body = response.json()
    assert "bookingid" in body
    assert body["booking"]["firstname"] == "Jim"

def test_get_booking_by_id():
    # create one first so we know a valid ID exists
    create_response = requests.post(f"{BASE_URL}/booking", json=sample_booking())
    booking_id = create_response.json()["bookingid"]

    get_response = requests.get(f"{BASE_URL}/booking/{booking_id}")
    assert get_response.status_code == 200
    assert get_response.json()["firstname"] == "Jim"

def test_update_booking(auth_token):
    create_response = requests.post(f"{BASE_URL}/booking", json=sample_booking())
    booking_id = create_response.json()["bookingid"]

    updated_data = sample_booking()
    updated_data["firstname"] = "James"

    update_response = requests.put(
        f"{BASE_URL}/booking/{booking_id}",
        json=updated_data,
        cookies={"token": auth_token}
    )
    assert update_response.status_code == 200
    assert update_response.json()["firstname"] == "James"

def test_delete_booking(auth_token):
    create_response = requests.post(f"{BASE_URL}/booking", json=sample_booking())
    booking_id = create_response.json()["bookingid"]

    delete_response = requests.delete(
        f"{BASE_URL}/booking/{booking_id}",
        cookies={"token": auth_token}
    )
    print(f"Actual status code: {delete_response.status_code}")
    assert delete_response.status_code == 201  # yes, 201 not 200 - restful-booker quirk

    # confirm it's actually gone
    get_response = requests.get(f"{BASE_URL}/booking/{booking_id}")
    assert get_response.status_code == 404
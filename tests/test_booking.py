import requests


def test_create_booking(base_url, booking_payload):
    response = requests.post(f"{base_url}/booking", json=booking_payload)
    assert response.status_code == 200
    body = response.json()
    assert "bookingid" in body
    assert body["booking"]["firstname"] == "Jim"


def test_get_booking_by_id(base_url, created_booking):
    booking_id = created_booking["bookingid"]

    get_response = requests.get(f"{base_url}/booking/{booking_id}")
    assert get_response.status_code == 200
    assert get_response.json()["firstname"] == "Jim"


def test_update_booking(base_url, auth_token, created_booking, booking_payload):
    booking_id = created_booking["bookingid"]

    updated_data = dict(booking_payload)
    updated_data["firstname"] = "James"

    update_response = requests.put(
        f"{base_url}/booking/{booking_id}",
        json=updated_data,
        cookies={"token": auth_token}
    )
    assert update_response.status_code == 200
    assert update_response.json()["firstname"] == "James"


def test_delete_booking(base_url, auth_token, created_booking):
    booking_id = created_booking["bookingid"]

    delete_response = requests.delete(
        f"{base_url}/booking/{booking_id}",
        cookies={"token": auth_token}
    )
    assert delete_response.status_code == 201  # yes, 201 not 200 - restful-booker quirk

    # confirm it's actually gone
    get_response = requests.get(f"{base_url}/booking/{booking_id}")
    assert get_response.status_code == 404


def test_get_booking_with_invalid_id_returns_404(base_url):
    response = requests.get(f"{base_url}/booking/999999999")
    assert response.status_code == 404


def test_update_booking_without_auth_token_is_rejected(base_url, created_booking, booking_payload):
    response = requests.put(
        f"{base_url}/booking/{created_booking['bookingid']}",
        json=booking_payload
        # no cookies/token passed
    )
    assert response.status_code in (401, 403)


def test_create_booking_with_missing_required_field(base_url, booking_payload):
    incomplete_booking = dict(booking_payload)
    del incomplete_booking["firstname"]
    response = requests.post(f"{base_url}/booking", json=incomplete_booking)

    # API returns a 500 with a plain-text body ("Internal Server Error")
    # instead of a proper 400 with a JSON error message. This is a
    # real API defect — see BUG-001 in this repo.
    assert response.status_code == 500
    assert response.text == "Internal Server Error"
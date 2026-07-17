def test_create_token_with_valid_credentials(base_url):
    import requests
    response = requests.post(
        f"{base_url}/auth",
        json={"username": "admin", "password": "password123"}
    )
    assert response.status_code == 200
    assert "token" in response.json()


def test_create_token_with_invalid_credentials(base_url):
    import requests
    response = requests.post(
        f"{base_url}/auth",
        json={"username": "wrong", "password": "wrong"}
    )
    assert response.status_code == 200  # this API returns 200 even on failure — worth noting!
    assert "token" not in response.json()
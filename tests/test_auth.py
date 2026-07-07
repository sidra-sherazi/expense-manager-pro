from tests.conftest import client


def test_register():

    response = client.post(
        "/auth/register",
        json={
            "username": "pytest",
            "email": "pytest@test.com",
            "password": "12345678",
        },
    )

    assert response.status_code == 200


def test_login():

    client.post(
        "/auth/register",
        json={
            "username": "pytest",
            "email": "pytest@test.com",
            "password": "12345678",
        },
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "pytest@test.com",
            "password": "12345678",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password():

    client.post(
        "/auth/register",
        json={
            "username": "pytest",
            "email": "pytest@test.com",
            "password": "12345678",
        },
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "pytest@test.com",
            "password": "wrongpassword",
        },
    )

    assert response.status_code == 401

    data = response.json()

    assert data["detail"] == "Incorrect email or password"


def test_protected_route_invalid_token():

    response = client.get(
        "/categories/",
        headers={
            "Authorization": "Bearer invalid_token",
        },
    )

    assert response.status_code == 401

    data = response.json()

    assert data["detail"] == "Invalid authentication credentials"
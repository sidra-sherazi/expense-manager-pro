from tests.conftest import client


def get_token():

    client.post(
        "/auth/register",
        json={
            "username": "categoryuser",
            "email": "category@test.com",
            "password": "12345678",
        },
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "category@test.com",
            "password": "12345678",
        },
    )

    token = response.json()["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }


def test_create_category():

    headers = get_token()

    response = client.post(
        "/categories/",
        json={
            "name": "Food"
        },
        headers=headers,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Food"


def test_get_categories():

    headers = get_token()

    client.post(
        "/categories/",
        json={
            "name": "Food"
        },
        headers=headers,
    )

    response = client.get(
        "/categories/",
        headers=headers,
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["name"] == "Food"


def test_update_category():

    headers = get_token()

    response = client.post(
        "/categories/",
        json={
            "name": "Food"
        },
        headers=headers,
    )

    category_id = response.json()["id"]

    response = client.put(
        f"/categories/{category_id}",
        json={
            "name": "Groceries"
        },
        headers=headers,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Groceries"


def test_delete_category():

    headers = get_token()

    response = client.post(
        "/categories/",
        json={
            "name": "Food"
        },
        headers=headers,
    )

    category_id = response.json()["id"]

    response = client.delete(
        f"/categories/{category_id}",
        headers=headers,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Category deleted successfully"
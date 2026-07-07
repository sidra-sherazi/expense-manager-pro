from tests.conftest import client


def get_token():

    client.post(
        "/auth/register",
        json={
            "username": "expenseuser",
            "email": "expense@test.com",
            "password": "12345678",
        },
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "expense@test.com",
            "password": "12345678",
        },
    )

    token = response.json()["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }


def create_category(headers):

    response = client.post(
        "/categories/",
        json={
            "name": "Food"
        },
        headers=headers,
    )

    return response.json()["id"]


def test_create_expense():

    headers = get_token()

    category_id = create_category(headers)

    response = client.post(
        "/expenses/",
        json={
            "title": "Pizza",
            "amount": 700,
            "description": "Dinner",
            "category_id": category_id,
        },
        headers=headers,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Pizza"
    assert data["amount"] == 700


def test_get_expenses():

    headers = get_token()

    category_id = create_category(headers)

    client.post(
        "/expenses/",
        json={
            "title": "Pizza",
            "amount": 700,
            "description": "Dinner",
            "category_id": category_id,
        },
        headers=headers,
    )

    response = client.get(
        "/expenses/",
        headers=headers,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["total"] == 1
    assert len(data["items"]) == 1


def test_update_expense():

    headers = get_token()

    category_id = create_category(headers)

    response = client.post(
        "/expenses/",
        json={
            "title": "Pizza",
            "amount": 700,
            "description": "Dinner",
            "category_id": category_id,
        },
        headers=headers,
    )

    expense_id = response.json()["id"]

    response = client.put(
        f"/expenses/{expense_id}",
        json={
            "title": "Burger",
            "amount": 900,
            "description": "Lunch",
            "category_id": category_id,
        },
        headers=headers,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Burger"
    assert data["amount"] == 900


def test_delete_expense():

    headers = get_token()

    category_id = create_category(headers)

    response = client.post(
        "/expenses/",
        json={
            "title": "Pizza",
            "amount": 700,
            "description": "Dinner",
            "category_id": category_id,
        },
        headers=headers,
    )

    expense_id = response.json()["id"]

    response = client.delete(
        f"/expenses/{expense_id}",
        headers=headers,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Expense deleted successfully"
import pytest
from faker import Faker

fake = Faker()


def test_users_get_all_without_auth(client):

    response = client.get("/users/")
    assert response.status_code == 401
    assert response.json() == {
        "message": "Please add a valid Authorization Header Ex: Bearer <token> or Token <token>"
    }


def test_get_all_users(client, auth):

    response = client.get("/users/", auth=auth)
    assert response.status_code == 200
    assert type(response.json()) == list


def test_create_and_delete_user(client, auth):

    user_data = {"username": fake.first_name(), "password": fake.text(10)}

    response = client.post("/users/", user_data, auth=auth)
    assert response.status_code == 201

    # Delete user
    location = response.headers.get("Content-Location")

    response = client.delete(location, auth=auth)
    assert response.status_code == 200


def test_get_user_by_id(client, user, auth):

    response = client.get(f"/users/{user.id}", auth=auth)
    assert response.status_code == 200
    assert response.json().get("username") == user.username


def test_update_user(client, user, auth):

    user_data = {"username": fake.first_name(), "password": fake.text(10)}

    response = client.put(f"/users/{user.id}", user_data, auth=auth)
    assert response.status_code == 200
    assert response.json() == {"message": "User update successfully"}


def test_get_user_not_found(client, number, auth):

    response = client.get(f"/users/{number}", auth=auth)
    assert response.status_code == 404
    assert response.json() == {"message": f"The user with id {number} not found"}

import pytest


def test_auth_login_with_wrong_credentials(client):

    userData = {"username": "", "password": ""}

    response = client.post("/auth/login", userData)
    assert response.status_code == 400
    assert response.json() == {"message": "Wrong credentials"}


def test_auth_login_without_password(client):

    userData = {"username": "featuren"}

    response = client.post("/auth/login", userData)
    assert response.status_code == 400
    assert response.json() == {"password": 'The "password" field is required.'}


def test_auth_login_without_password(client):

    userData = {"password": "secret"}

    response = client.post("/auth/login", userData)
    assert response.status_code == 400
    assert response.json() == {"username": 'The "username" field is required.'}


def test_auth_login_successfully(client, user):

    userData = {"username": user.username, "password": user.password}

    response = client.post("/auth/login", userData)
    assert response.status_code == 200

    user.delete()


def test_auth_login_without_credentials(client):

    response = client.post("/auth/login")
    assert response.status_code == 400
    assert response.json() == "May not be null."

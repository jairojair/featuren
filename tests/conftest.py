import pytest
import secrets
from app import app
from random import randint
from apistar import TestClient
from models.user import User
from models.service import Service
from faker import Faker

fake = Faker()


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def number():
    return randint(0, 10000)


@pytest.fixture()
def user():

    fake = Faker()

    user_data = {"username": fake.first_name(), "password": fake.text(10)}

    user = User()
    user.create(user_data)
    user.password = user_data.get("password")

    return user


@pytest.fixture()
def service():

    service_data = {"name": fake.first_name(), "description": fake.text(100)}
    service = Service.create(**service_data, token=secrets.token_urlsafe(31))
    yield service
    service.delete()


@pytest.fixture()
def auth(client, user):
    def auth(request):

        userData = {"username": user.username, "password": user.password}

        response = client.post("/auth/login", userData)
        token = response.json().get("token")

        request.headers["authorization"] = f"Bearer {token}"
        return request

    yield auth
    user.delete()

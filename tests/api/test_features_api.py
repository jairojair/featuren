import pytest
from faker import Faker

fake = Faker()


def test_get_all_features_without_auth(client):

    response = client.get("/features/")
    assert response.status_code == 401
    assert response.json() == {
        "message": "Please add a valid Authorization Header Ex: Bearer <token> or Token <token>"
    }


"""

Auth by Authorization token

"""


def test_get_all_features_by_service_with_wrong_token(client):

    headers = {"authorization": f"Token 1"}

    response = client.get("/features/", headers=headers)

    assert response.status_code == 401
    assert response.json() == {"message": "Unauthorized, invalid token"}


def test_get_all_features_by_service_token(client, service):

    headers = {"authorization": f"Token {service.token}"}

    response = client.get("/features/", headers=headers)

    assert response.status_code == 200
    assert type(response.json()) == list


"""

Auth by Authorization Bearer

"""


def test_get_all_features(client, auth):

    response = client.get("/features/", auth=auth)
    assert response.status_code == 200
    assert type(response.json()) == list


def test_create_feature_without_data(client, auth):

    feature = {}

    response = client.post("/features/", feature, auth=auth)
    assert response.status_code == 400
    assert response.json() == "May not be null."


def test_create_feature_without_id(client, auth):

    feature = {"version": "1.0.0", "enabled": True, "deny": False, "services": []}

    response = client.post("/features/", json=feature, auth=auth)
    assert response.status_code == 400
    assert response.json() == {"id": 'The "id" field is required.'}


def test_create_feature_services_with_duplicated_items(client, auth):

    feature = {
        "id": fake.first_name(),
        "version": "1.0.0",
        "enabled": True,
        "deny": False,
        "services": [2, 2],
    }

    response = client.post("/features/", json=feature, auth=auth)
    assert response.status_code == 400
    assert response.json() == {"services": {"1": "This item is not unique."}}


def test_create_feature_services_with_wront_type(client, auth):

    feature = {
        "id": fake.first_name(),
        "version": "1.0.0",
        "enabled": True,
        "deny": False,
        "services": ["x", 2],
    }

    response = client.post("/features/", json=feature, auth=auth)
    assert response.status_code == 400
    assert response.json() == {"services": {"0": "Must be a number."}}


def test_create_and_delete_feature(client, auth):

    feature = {
        "id": fake.first_name(),
        "version": "1.0.0",
        "enabled": True,
        "deny": False,
        "services": [],
    }

    response = client.post("/features/", json=feature, auth=auth)
    assert response.status_code == 201

    # delete feature
    location = response.headers.get("Content-Location")

    response = client.delete(location, auth=auth)
    assert response.status_code == 200
    assert response.json() == {"message": "Feature deleted successfully."}


def test_get_feature_not_found(client, number, auth):

    response = client.get(f"/features/{number}", auth=auth)
    assert response.status_code == 404
    assert response.json() == {"message": f"Feature not found."}

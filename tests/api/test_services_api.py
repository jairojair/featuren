import pytest
from faker import Faker

fake = Faker()


def test_get_all_services_without_auth(client):

    response = client.get("/services/")
    assert response.status_code == 401
    assert response.json() == {
        "message": "Please add a valid Authorization Header Ex: Bearer <token> or Token <token>"
    }


def test_get_all_services(client, auth):

    response = client.get("/services/", auth=auth)
    assert response.status_code == 200
    assert type(response.json()) == list


def test_create_and_delete_service(client, auth):

    service_data = {"name": fake.first_name(), "description": fake.text(100)}

    response = client.post("/services/", service_data, auth=auth)
    assert response.status_code == 201

    # delete service
    location = response.headers.get("Content-Location")

    response = client.delete(location, auth=auth)
    assert response.status_code == 200
    assert response.json() == {"message": "Service deleted successfully"}


def test_get_service_by_id(client, service, auth):

    response = client.get(f"/services/{service.id}", auth=auth)
    assert response.status_code == 200
    assert response.json().get("name") == service.name


def test_get_service_not_found(client, number, auth):

    response = client.get(f"/services/{number}", auth=auth)
    assert response.status_code == 404
    assert response.json() == {"message": f"The service with id {number} not found"}

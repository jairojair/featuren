import secrets
import logging
from apistar import Route, http, exceptions
from models.service import Service, ServiceType

log = logging.getLogger(__name__)


def get_services():
    """
    Return all services
    """
    services = Service.all()
    return services.serialize()


def create_service(serviceData: ServiceType):
    """
    Create a new service
    """

    service = Service.create(**serviceData, token=secrets.token_urlsafe(31))

    msg = "Service created successfully."
    log.info(f"{msg} - ID: {service.id}")

    headers = {"Content-Location": f"/services/{service.id}"}
    return http.JSONResponse({"message": msg}, status_code=201, headers=headers)


def get_service(id):
    """
    Get service information
    """
    service = Service.find(id)

    if not service:
        msg = f"Service not found."
        raise exceptions.NotFound({"message": msg})

    return service.serialize()


def delete_service(id):
    """
    Delete a service
    """

    service = Service.find(id)

    if not service:
        msg = f"Service not found."
        raise exceptions.NotFound({"message": msg})

    service.delete()
    msg = "Service deleted successfully."
    log.info(f"{msg} - ID: {id}")
    return {"message": msg}


routes = [
    Route("/", method="GET", handler=get_services, name="Get all services"),
    Route("/", method="POST", handler=create_service, name="Create"),
    Route("/{id}", method="GET", handler=get_service, name="Get service"),
    Route("/{id}", method="DELETE", handler=delete_service, name="Delete"),
]

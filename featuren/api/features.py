import re
import logging
from apistar import Route, http, exceptions
from models.feature import Feature, FeatureCreate, FeatureUpdate
from models.service import Service

from components.auth import AuthData

log = logging.getLogger(__name__)


def get_features(auth: AuthData):
    """
    This handler function return features by service or all features.
    """

    if auth.user:
        return Feature.all().serialize()

    features = _set_visible_only(["id", "version"], auth.service.features)
    return features.serialize()


def create_feature(featureData: FeatureCreate):
    """
    Create a new feature
    """

    _check_id_format(featureData.id)
    _check_version_format(featureData.version)

    if Feature.find(featureData.id):
        msg = f"The feature id isn't available. Please try another."
        return http.JSONResponse({"message": msg}, status_code=409)

    _check_services_exists(featureData.services)

    feature = Feature.create(**featureData)
    msg = "Feature created successfully."
    log.info(f"{msg} - ID: {feature.id}")

    feature.update_services(featureData.services)

    headers = {"Content-Location": f"/features/{feature.id}"}
    return http.JSONResponse({"message": msg}, status_code=201, headers=headers)


def get_feature(auth: AuthData, id):
    """
    Get feature
    """

    log.info(f"Get feature by id: {id}")

    feature = _find_feature(id)

    if auth.user:
        return feature.serialize()

    feature.set_visible(["id", "version"])
    _check_rules(feature, auth)
    return feature.serialize()


def update_feature(auth: AuthData, featureData: FeatureUpdate, id):
    """
    Update Feature information
    """

    feature = _find_feature(id)

    _check_version_format(featureData.version)

    if auth.user:
        _check_services_exists(featureData.services)
        feature.update_services(featureData.services)

    else:
        _check_rules(feature, auth)

    feature.update(**featureData)

    msg = "Feature update successfully."
    log.info(f"{msg} - ID: {id}")
    return {"message": msg}


def delete_feature(id):
    """
    Delete a feature
    """

    feature = _find_feature(id)
    feature.delete()
    msg = "Feature deleted successfully."
    log.info(f"{msg} - ID: {id}")
    return {"message": msg}


"""
Privates functions
"""


def _check_rules(feature, auth):

    if feature.enabled:
        return

    query = auth.service.features.where("id", feature.id).first()

    if feature.deny:
        query = not query

    if not query:
        msg = f"Access denied to resource."
        log.info(f"{msg} - ID: {id}, service: {auth.service.name}")
        raise exceptions.Forbidden({"message": msg})


def _find_feature(id):
    """
    Find a feature by id
    """

    feature = Feature.find(id)

    if not feature:
        msg = f"Feature not found."
        raise exceptions.NotFound({"message": msg})

    return feature


def _find_service(id):
    """
    Find a service by id
    """

    service = Service.find(id)

    if not service:
        msg = f"Service not found"
        raise exceptions.NotFound({"services": msg})


def _check_services_exists(services):
    """
    This function check if services exists.
    """

    if services is None:
        return

    for service in services:
        _find_service(service)


def _set_visible_only(values, features):
    """
    This function return only values.
    """
    return features.transform(lambda item: item.set_visible(values))


def _check_version_format(version):
    """
    This function check the version format.
    """

    version_format = "^[\d].[\d].[\d]$"

    if not re.match(version_format, version):
        msg = "The version format is invalid. The correct is (Example: 1.0.0)."
        raise exceptions.BadRequest({"message": msg})


def _check_id_format(feature_id):
    """
    This function check the id format.
    """

    id_format = "^(\w+).+\S$"

    if not re.match(id_format, feature_id):
        msg = "The id field cannot contains whitespaces."
        raise exceptions.BadRequest({"message": msg})


routes = [
    Route("/", method="GET", handler=get_features, name="Get all features"),
    Route("/", method="POST", handler=create_feature, name="Create"),
    Route("/{id}", method="GET", handler=get_feature, name="Get a feature"),
    Route("/{id}", method="PUT", handler=update_feature, name="Update"),
    Route("/{id}", method="DELETE", handler=delete_feature, name="Delete"),
]

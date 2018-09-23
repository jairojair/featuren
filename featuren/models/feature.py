from apistar import types, validators
from orator import Model, accessor
from models.features_service import FeaturesServices

import logging

log = logging.getLogger(__name__)


class FeatureUpdate(types.Type):

    version = validators.String(description="The feature number version.")
    enabled = validators.Boolean()
    deny = validators.Boolean()

    services = validators.Array(
        unique_items=True,
        items=validators.Integer(),
        allow_null=True,
        description="Array with services allowed to access the feature.",
    )


class FeatureCreate(FeatureUpdate):

    id = validators.String(min_length=3, max_length=30, description="Feature name.")


class Feature(Model):

    __table__ = "features"
    __timestamps__ = False

    __fillable__ = ["id", "version", "enabled", "deny"]

    __appends__ = ["services"]

    @accessor
    def services(self):
        """
        Method to get all services by feature.
        """
        services = FeaturesServices.all().where("feature_id", self.id)
        services.transform(lambda item: item.service_id)

        return services.serialize()

    def update_services(self, services):
        """
        Method to update the list of available services for feature.
        """

        try:

            FeaturesServices.where("feature_id", self.id).delete()

            if services:

                for service in services:
                    FeaturesServices.create(feature_id=self.id, service_id=service)

        except Exception as e:
            log.info(e)

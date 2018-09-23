from apistar import types, validators
from orator import Model
from orator.orm import belongs_to_many
from models.feature import Feature


class ServiceType(types.Type):

    name = validators.String(max_length=30, description="The service name.")
    description = validators.String(
        max_length=100, description="The service description."
    )


class Service(Model):

    __table__ = "services"
    __timestamps__ = False

    __fillable__ = ["name", "description", "token"]

    @belongs_to_many
    def features(self):
        return Feature

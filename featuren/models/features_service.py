from orator import Model


class FeaturesServices(Model):

    __table__ = "features_services"
    __fillable__ = ["feature_id", "service_id"]
    __timestamps__ = False

import logging
from apistar import Route

log = logging.getLogger(__name__)


def status():
    """
    Status
    """

    ret = {
        "message": "Welcome to Featuren!",
        "documentation": "https://jairojair.github.io/featuren/",
    }
    return ret


routes = [Route("/", "GET", status)]

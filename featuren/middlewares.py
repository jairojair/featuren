import logging
from components.auth import AuthData

log = logging.getLogger(__name__)


class EventHookAuth:
    """
    This event hook (middleware) check information about authentication.
    """

    def on_request(self, auth: AuthData):
        pass

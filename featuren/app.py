from wsgicors import CORS
from apistar import App, Include

from settings import jwt_settings

from components.auth import Auth
from middlewares import EventHookAuth

from api import auth
from api import users
from api import status
from api import features
from api import services

components = [Auth(jwt_settings)]
event_hooks = [EventHookAuth()]

routes = [
    Include("/", name="Status", routes=status.routes),
    Include("/auth", name="Authentication", routes=auth.routes),
    Include("/users", name="User", routes=users.routes),
    Include("/features", name="Feature", routes=features.routes),
    Include("/services", name="Service", routes=services.routes),
]

app = App(routes=routes, components=components, event_hooks=event_hooks)
app = CORS(app, headers="*", methods="*", origin="*", maxage="86400")

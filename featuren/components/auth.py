import jwt
import logging
from apistar import exceptions, http, Route
from apistar.server.components import Component
from models.user import User
from models.service import Service

log = logging.getLogger(__name__)


class AuthData:
    def __init__(self, user=None, service=None):
        self.user = user
        self.service = service


class Auth(Component):
    """
    This component get a User by token
    """

    no_auth_list = ["login", "serve_documentation", "serve_schema", "status"]

    accept_token_list = ["get_features", "get_feature", "update_feature"]

    def __init__(self, settings):

        self.secret = settings.get("secret")
        self.algorithms = settings.get("algorithms")

    def raise_about_authorization_format(self):
        """
        Describe
        """

        msg = "Please add a valid Authorization Header Ex: Bearer <token> or Token <token>"
        raise exceptions.HTTPException({"message": msg}, status_code=401)

    def get_data_by_header(self, authorization):
        """
        Describe
        """

        if not authorization:
            self.raise_about_authorization_format()

        try:

            scheme, token = authorization.split()

            if scheme == "Bearer" or scheme == "Token":
                return scheme, token

            self.raise_about_authorization_format()

        except ValueError:
            self.raise_about_authorization_format()

    def resolve(self, authorization: http.Header, route: Route) -> AuthData:
        """
        Describe
        """

        if route.handler.__name__ in self.no_auth_list:

            log.info(f"No auth handler")
            return AuthData()

        scheme, token = self.get_data_by_header(authorization)

        if "Bearer" in scheme:

            try:

                payload = jwt.decode(token, self.secret, self.algorithms)
                user_id = payload.get("user_id")

                user = User.find(user_id)

                if user is None:
                    msg = "Unauthorized, invalid token"
                    raise exceptions.HTTPException({"message": msg}, status_code=401)

                return AuthData(user, None)

            except jwt.DecodeError:

                msg = "Unauthorized, invalid token"
                raise exceptions.HTTPException({"message": msg}, status_code=401)

            except jwt.ExpiredSignatureError:

                msg = "Unauthorized, token expired"
                raise exceptions.HTTPException({"message": msg}, status_code=401)

        if "Token" in scheme:

            if route.handler.__name__ in self.accept_token_list:

                service = Service.where("token", token).first()

                if service is None:
                    msg = "Unauthorized, invalid token"
                    raise exceptions.HTTPException({"message": msg}, status_code=401)

                return AuthData(None, service)

            msg = f"This endpoint is not available by Token, please use Bearer header"
            raise exceptions.Forbidden({"message": msg})

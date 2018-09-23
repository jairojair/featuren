import jwt
import logging
from datetime import datetime, timedelta
from apistar import Route, http, exceptions
from settings import jwt_settings
from models.user import User, UserType

log = logging.getLogger(__name__)


def login(userData: UserType):
    """
    Login
    """
    user = User.where("username", userData.username).first()

    if user and user.check_password(userData.password):

        log.info(f"Login user with id: {user.id} successfully")

        payload = {
            "user_id": user.id,
            "exp": datetime.utcnow() + timedelta(seconds=jwt_settings.get("exp")),
        }

        token = jwt.encode(
            payload, jwt_settings.get("secret"), jwt_settings.get("algorithm")
        )
        return http.JSONResponse({"token": token.decode("utf-8")})

    msg = f"Wrong credentials"
    return http.JSONResponse({"message": msg}, status_code=400)


routes = [Route("/login", "POST", handler=login, name="Login")]

import logging
from apistar import Route, http, exceptions
from models.user import User, UserType

log = logging.getLogger(__name__)


def users_list():
    """
    Return all users
    """

    users = User.all()
    return users.serialize()


def create_user(userData: UserType):
    """
    Create a new user
    """

    if User.check_username(userData.username):
        msg = f"The username: {userData.username} isn't available. Please try another."
        return http.JSONResponse({"message": msg}, status_code=409)

    user = User()
    user = user.create(userData)

    msg = "User created successfully."
    log.info(f"{msg} - ID: {user.id}")

    headers = {"Content-Location": f"/users/{user.id}"}
    return http.JSONResponse({"message": msg}, status_code=201, headers=headers)


def get_user(id):
    """
    Get user information
    """
    user = User.find(id)

    if not user:
        msg = f"User not found."
        raise exceptions.NotFound({"message": msg})

    return user.serialize()


def update_user(userData: UserType, id):
    """
    Update user information
    """
    user = User.find(id)

    if not user:
        msg = f"User not found."
        raise exceptions.NotFound({"message": msg})

    user.update(**userData)

    msg = "User update successfully."
    log.info(f"{msg} - ID: {id}")
    return {"message": msg}


def delete_user(id):
    """
    Delete a user
    """

    user = User.find(id)

    if not user:
        msg = f"User not found."
        raise exceptions.NotFound({"message": msg})

    user.delete()
    msg = "User deleted successfully."
    log.info(f"{msg} - ID: {id}")
    return {"message": msg}


routes = [
    Route("/", method="GET", handler=users_list, name="Get all users"),
    Route("/", method="POST", handler=create_user, name="Create"),
    Route("/{id}", method="GET", handler=get_user, name="Get a user"),
    Route("/{id}", method="PUT", handler=update_user, name="Update"),
    Route("/{id}", method="DELETE", handler=delete_user, name="Delete"),
]

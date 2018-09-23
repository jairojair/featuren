from apistar import types, validators
from passlib.hash import pbkdf2_sha256
from orator import Model


class UserType(types.Type):

    username = validators.String(max_length=30, description="The username is unique.")
    password = validators.String(max_length=30, description="The user password.")


class User(Model):

    __table__ = "users"
    __timestamps__ = False

    __hidden__ = ["password"]

    __fillable__ = ["username", "password"]

    def create(self, data):

        self.username = data.get("username")
        self.password = pbkdf2_sha256.hash(data.get("password"))
        self.admin = bool(data.get("admin"))

        if self.save():
            return self

    def check_password(self, password):
        return pbkdf2_sha256.verify(password, self.password)

    def check_username(username):
        return User.where("username", username).first()

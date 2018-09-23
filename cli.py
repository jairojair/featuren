import click

from featuren.settings import db
from featuren.models.user import User


@click.group()
def cli():
    pass


def validate_user(ctx, param, value):
    """
    User validation.
    """

    user = User.where("username", value).first()

    if user:
        click.secho(f"Username: {value} already exists, please try other one.", **ERROR)
        raise click.Abort

    return value


@cli.command()
@click.option("--username", callback=validate_user, prompt=True)
@click.password_option()
def add_user(username, password):
    """
    Command to add new user.
    """

    user_data = {"username": username, "password": password}

    try:
        user = User()
        user.create(user_data)
        click.secho(f"User: {username} create successfully!", **SUCCESS)
    except Exception:
        click.secho(f"Please try again", **ERROR)


# custom styles #

SUCCESS = dict(bg="green", fg="white")
ERROR = dict(bg="red", fg="white")

cli()

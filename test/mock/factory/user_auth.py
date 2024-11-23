from polyfactory.factories import DataclassFactory

from src.apps.user_auth.domain.commands import (
    AuthorizeUserAuthCommand,
    LoginUserAuthCommand,
)
from src.apps.user_auth.domain.entities import UserAuth


class UserAuthFactory(DataclassFactory[UserAuth]):
    __model__ = UserAuth


class AuthorizeUserAuthCommandFactory(DataclassFactory[AuthorizeUserAuthCommand]):
    __model__ = AuthorizeUserAuthCommand


class LoginUserAuthCommandFactory(DataclassFactory[LoginUserAuthCommand]):
    __model__ = LoginUserAuthCommand

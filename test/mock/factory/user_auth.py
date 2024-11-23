from polyfactory.factories import DataclassFactory

from src.apps.customer.domain.commands import (
    AuthorizeCustomerCommand,
    LoginCustomerCommand,
)
from src.apps.customer.domain.entities import Customer


class CustomerFactory(DataclassFactory[Customer]):
    __model__ = Customer


class AuthorizeCustomerCommandFactory(DataclassFactory[AuthorizeCustomerCommand]):
    __model__ = AuthorizeCustomerCommand


class LoginCustomerCommandFactory(DataclassFactory[LoginCustomerCommand]):
    __model__ = LoginCustomerCommand

from dataclasses import dataclass

from src.apps.customer.domain.commands import (
    AuthorizeCustomerCommand,
    GetCustomerCommand,
    LoginCustomerCommand,
)
from src.apps.customer.domain.entities import Customer
from src.apps.customer.domain.services import (
    ICodeService,
    ICustomerService,
    ILoginService,
    ISendCodeService,
)


@dataclass(frozen=True)
class GetCustomerUseCase:
    customer_service: ICustomerService

    def execute(self, command: GetCustomerCommand) -> Customer:
        return self.customer_service.get_by_token(token=command.token)


@dataclass(frozen=True)
class AuthorizeCustomerUseCase:
    code_service: ICodeService
    send_code_service: ISendCodeService
    customer_service: ICustomerService

    def execute(self, command: AuthorizeCustomerCommand) -> str:
        user = self.customer_service.get_or_create(customer=command.customer)
        code = self.code_service.generate_code(
            phone_number=user.phone_number, email=user.email
        )
        self.send_code_service.send_code(
            code=code, phone_number=user.phone_number, email=user.email
        )
        return code


@dataclass(frozen=True)
class LoginCustomerUseCase:
    code_service: ICodeService
    login_service: ILoginService
    customer_service: ICustomerService

    def execute(self, command: LoginCustomerCommand) -> str:
        customer = self.customer_service.get_by_phone_number_or_email(
            phone_number=command.phone_number, email=command.email
        )
        self.code_service.validate_code(
            code=command.code,
            phone_number=customer.phone_number,
            email=customer.email,
        )
        token = self.login_service.active_and_generate_token(customer)
        self.customer_service.update(customer)
        return token

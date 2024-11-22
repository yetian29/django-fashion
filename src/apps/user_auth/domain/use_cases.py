from dataclasses import dataclass

from src.apps.user_auth.domain.commands import (
    AuthorizeUserAuthCommand,
    LoginUserAuthCommand,
)
from src.apps.user_auth.domain.services import (
    ICodeService,
    ILoginService,
    ISendCodeService,
    IUserAuthService,
)


@dataclass(frozen=True)
class AuthorizeUserAuthUseCase:
    code_service: ICodeService
    send_code_service: ISendCodeService
    user_auth_service: IUserAuthService

    def execute(self, command: AuthorizeUserAuthCommand) -> str:
        user = self.user_auth_service.get_or_create(user_auth=command.user_auth)
        code = self.code_service.generate_code(
            phone_number=user.phone_number, email=user.email
        )
        self.send_code_service.send_code(
            code=code, phone_number=user.phone_number, email=user.email
        )
        return code


@dataclass(frozen=True)
class LoginUserAuthUseCase:
    code_service: ICodeService
    login_service: ILoginService
    user_auth_service: IUserAuthService

    def execute(self, command: LoginUserAuthCommand) -> str:
        user = self.user_auth_service.get_by_phone_number_or_email(
            phone_number=command.phone_number, email=command.email
        )
        self.code_service.validate_code(
            phone_number=user.phone_number, email=user.email
        )
        token = self.login_service.active_and_generate_token(user)
        self.user_auth_service.update(user)
        return token

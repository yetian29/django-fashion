import random

from src.apps.user_auth.domain.services import (
    ICodeService,
    ILoginService,
    ISendCodeService,
    IUserAuthService,
)


class CodeService(ICodeService):
    def generate_code(
        self, phone_number: str | None = None, email: str | None = None
    ) -> str:
        code = random.randint(100000, 999999)

        return code


class SendService(ISendCodeService):
    pass


class LoginService(ILoginService):
    pass


class UserAuthService(IUserAuthService):
    pass

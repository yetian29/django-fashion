from dataclasses import dataclass

from src.apps.user_auth.domain.entities import UserAuth


@dataclass(frozen=True)
class AuthorizeUserAuthCommand:
    user: UserAuth


@dataclass(frozen=True)
class LoginUserAuthCommand:
    phone_number: str
    email: str
    code: str

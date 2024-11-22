import random
from dataclasses import dataclass
from datetime import datetime, timedelta
from uuid import uuid4

from django.core.cache import cache

from src.apps.user_auth.domain.entities import UserAuth
from src.apps.user_auth.domain.errors import (
    CachedDataAreNotFoundException,
    CodeIsExpiredException,
    CodesAreNotEqualException,
    UserAuthIsNotFoundException,
)
from src.apps.user_auth.domain.services import (
    ICodeService,
    ILoginService,
    ISendCodeService,
    IUserAuthService,
)
from src.apps.user_auth.infrastructure.models import UserAuthORM
from src.apps.user_auth.infrastructure.repositories import IUserAuthRepository
from src.helper import fail


class CodeService(ICodeService):
    def generate_code(
        self, phone_number: str | None = None, email: str | None = None
    ) -> str:
        code = random.randint(100000, 999999)
        ttl = timedelta(minutes=1)
        cached_data = {"code": code, "expire_time": datetime.now() + ttl}
        key = phone_number if phone_number else email
        cache.set(key, cached_data)
        return code

    def validate_code(
        self, code: str, phone_number: str | None = None, email: str | None = None
    ) -> None:
        key = phone_number if phone_number else email
        cached_data = cache.get(key)
        if not cached_data:
            fail(CachedDataAreNotFoundException)
        elif datetime.now() > cached_data.get("expire_time"):
            del cache[key]
            fail(CodeIsExpiredException)
        elif code != cached_data.get("code"):
            del cache[key]
            fail(CodesAreNotEqualException)
        del cache[key]


class SendCodeService(ISendCodeService):
    def send_code(
        self, code: str, phone_number: str | None = None, email: str | None = None
    ) -> None:
        key = phone_number if phone_number else email
        print(f"The code <{code}> has been sent to phone number or email <{key}>")


class LoginService(ILoginService):
    def active_and_generate_token(self, user_auth: UserAuth) -> str:
        user_auth.is_active = True
        user_auth.token = str(uuid4())
        return user_auth.token


@dataclass(frozen=True)
class UserAuthService(IUserAuthService):
    repository: IUserAuthRepository

    def get_by_phone_number_or_email(
        self, phone_number: str | None = None, email: str | None = None
    ) -> UserAuth:
        if phone_number:
            user_auth_orm = self.repository.get_by_phone_number(phone_number)
        else:
            user_auth_orm = self.repository.get_by_email(email)
        if not user_auth_orm:
            fail(UserAuthIsNotFoundException)
        return user_auth_orm.to_entity()

    def get_or_create(self, user_auth: UserAuth) -> UserAuth:
        try:
            return self.get_by_phone_number_or_email(
                phone_number=user_auth.phone_number, email=user_auth.email
            )
        except UserAuthIsNotFoundException:
            user_auth_orm = UserAuthORM.from_entity(user_auth)
            user_auth_orm = self.repository.create(user_auth_orm=user_auth_orm)
            return user_auth_orm.to_entity()

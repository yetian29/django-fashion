import random
from datetime import datetime, timedelta
from typing import Any
from uuid import uuid4

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
from src.helper import fail
from test.mock.factory.user_auth import UserAuthFactory


class DummyCodeService(ICodeService):
    def __init__(self) -> dict:
        self.cache: dict[str, dict[str, Any]] = {}

    def generate_code(
        self, phone_number: str | None = None, email: str | None = None
    ) -> str:
        code = str(random.randint(100000, 999999))
        ttl = timedelta(minutes=1)
        cached_data = {"code": code, "expire_time": datetime.now() + ttl}
        key = phone_number if phone_number else email
        self.cache[key] = cached_data
        return code

    def validate_code(
        self, code: str, phone_number: str | None = None, email: str | None = None
    ) -> None:
        key = phone_number if phone_number else email
        cached_data = self.cache.get(key)
        if not cached_data:
            fail(CachedDataAreNotFoundException)
        elif datetime.now() > cached_data.get("expire_time"):
            del self.cache[key]
            fail(CodeIsExpiredException)
        elif code != cached_data.get("code"):
            del self.cache[key]
            fail(CodesAreNotEqualException)
        del self.cache[key]


class DummySendCodeService(ISendCodeService):
    def send_code(
        self, code: str, phone_number: str | None = None, email: str | None = None
    ) -> None:
        key = phone_number if phone_number else email
        print(f"The code <{code}> has been to sent to phone number or email <{key}>")


class DummyLoginService(ILoginService):
    def active_and_generate_token(self, user_auth: UserAuth) -> str:
        user_auth.is_active = True
        user_auth.token = uuid4()
        user_auth.updated_at = datetime.now()
        return user_auth.token


class DummyUserAuthService(IUserAuthService):
    def get_by_phone_number_or_email(
        self, phone_number: str | None = None, email: str | None = None
    ) -> UserAuth:
        if phone_number:
            return UserAuthFactory.build(phone_number=phone_number)
        return UserAuthFactory.build(email=email)

    def get_or_create(self, user_auth: UserAuth) -> UserAuth:
        try:
            return self.get_by_phone_number_or_email(
                phone_number=user_auth.phone_number, email=user_auth.email
            )
        except UserAuthIsNotFoundException:
            user_auth.oid = uuid4()
            user_auth.created_at = datetime.now()
            user_auth.updated_at = datetime.now()
            return user_auth

    def update(self, user_auth: UserAuth) -> UserAuth:
        return user_auth

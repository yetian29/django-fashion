import random
from datetime import datetime, timedelta
from typing import Any
from uuid import uuid4

from src.apps.customer.domain.entities import Customer
from src.apps.customer.domain.errors import (
    CachedDataAreNotFoundException,
    CodeIsExpiredException,
    CodesAreNotEqualException,
    CustomerIsNotFoundException,
)
from src.apps.customer.domain.services import (
    ICodeService,
    ICustomerService,
    ILoginService,
    ISendCodeService,
)
from src.helper import fail
from test.mock.factory.customer import CustomerFactory


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
    def active_and_generate_token(self, customer: Customer) -> str:
        customer.is_active = True
        customer.token = uuid4()
        customer.updated_at = datetime.now()
        return customer.token


class DummyCustomerService(ICustomerService):
    def get_by_phone_number_or_email(
        self, phone_number: str | None = None, email: str | None = None
    ) -> Customer:
        if phone_number:
            return CustomerFactory.build(phone_number=phone_number)
        return CustomerFactory.build(email=email)

    def get_or_create(self, customer: Customer) -> Customer:
        try:
            return self.get_by_phone_number_or_email(
                phone_number=customer.phone_number, email=customer.email
            )
        except CustomerIsNotFoundException:
            customer.oid = uuid4()
            customer.created_at = datetime.now()
            customer.updated_at = datetime.now()
            return customer

    def update(self, customer: Customer) -> Customer:
        return customer

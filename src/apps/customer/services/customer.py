import random
from dataclasses import dataclass
from datetime import datetime, timedelta
from uuid import UUID, uuid4

from django.core.cache import cache

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
from src.apps.customer.infrastructure.repositories import ICustomerRepository
from src.helper import fail


class CodeService(ICodeService):
    def generate_code(
        self, phone_number: str | None = None, email: str | None = None
    ) -> str:
        code = str(random.randint(100000, 999999))
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
            cache.delete(key)
            fail(CodeIsExpiredException)
        elif code != cached_data.get("code"):
            cache.delete(key)
            fail(CodesAreNotEqualException)
        cache.delete(key)


class SendCodeService(ISendCodeService):
    def send_code(
        self, code: str, phone_number: str | None = None, email: str | None = None
    ) -> None:
        key = phone_number if phone_number else email
        print(f"The code <{code}> has been sent to phone number or email <{key}>")


class LoginService(ILoginService):
    def active_and_generate_token(self, customer: Customer) -> UUID:
        customer.is_active = True
        customer.token = uuid4()
        customer.updated_at = datetime.now()
        return customer.token


@dataclass(frozen=True)
class CustomerService(ICustomerService):
    repository: ICustomerRepository

    def get_by_phone_number_or_email(
        self, phone_number: str | None = None, email: str | None = None
    ) -> Customer:
        if phone_number:
            customer_orm = self.repository.get_by_phone_number(phone_number)
        else:
            customer_orm = self.repository.get_by_email(email)
        if not customer_orm:
            fail(CustomerIsNotFoundException)
        return customer_orm.to_entity()

    def get_or_create(self, customer: Customer) -> Customer:
        try:
            return self.get_by_phone_number_or_email(
                phone_number=customer.phone_number, email=customer.email
            )
        except CustomerIsNotFoundException:
            customer_orm = self.repository.create(
                phone_number=customer.phone_number, email=customer.email
            )
            return customer_orm.to_entity()

    def get_by_token(self, token: UUID) -> Customer:
        customer_orm = self.repository.get_by_token(token)
        if not customer_orm:
            fail(CustomerIsNotFoundException)
        return customer_orm.to_entity()

    def update(self, customer: Customer) -> Customer:
        return self.repository.update(customer=customer)

from abc import ABC, abstractmethod
from uuid import UUID

from src.apps.customer.domain.entities import Customer
from src.apps.customer.infrastructure.models import CustomerORM


class ICustomerRepository(ABC):
    @abstractmethod
    def get_by_phone_number(self, phone_number: str) -> CustomerORM | None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> CustomerORM | None:
        pass

    @abstractmethod
    def get_by_token(self, token: UUID) -> CustomerORM | None:
        pass

    @abstractmethod
    def create(
        self, phone_number: str | None = None, email: str | None = None
    ) -> CustomerORM:
        pass

    @abstractmethod
    def update(self, customer: Customer) -> CustomerORM:
        pass


class PostgresCustomerRepository(ICustomerRepository):
    def get_by_phone_number(self, phone_number: str) -> CustomerORM | None:
        try:
            return CustomerORM.objects.get(phone_number=phone_number)
        except CustomerORM.DoesNotExist:
            return None

    def get_by_email(self, email: str) -> CustomerORM | None:
        try:
            return CustomerORM.objects.get(email=email)
        except CustomerORM.DoesNotExist:
            return None

    def get_by_token(self, token: UUID) -> CustomerORM | None:
        try:
            return CustomerORM.objects.get(token=token)
        except CustomerORM.DoesNotExist:
            return None

    def create(
        self, phone_number: str | None = None, email: str | None = None
    ) -> CustomerORM:
        if phone_number:
            return CustomerORM.objects.create(phone_number=phone_number)
        return CustomerORM.objects.create(email=email)

    def update(self, customer: Customer) -> CustomerORM:
        return CustomerORM.objects.filter(oid=customer.oid).update(
            is_active=customer.is_active,
            token=customer.token,
            updated_at=customer.updated_at,
        )

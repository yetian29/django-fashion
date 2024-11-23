from abc import ABC, abstractmethod

from src.apps.user_auth.domain.entities import UserAuth
from src.apps.user_auth.infrastructure.models import UserAuthORM


class IUserAuthRepository(ABC):
    @abstractmethod
    def get_by_phone_number(self, phone_number: str) -> UserAuthORM | None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> UserAuthORM | None:
        pass

    @abstractmethod
    def create(
        self, phone_number: str | None = None, email: str | None = None
    ) -> UserAuthORM:
        pass

    @abstractmethod
    def update(self, user_auth: UserAuth) -> UserAuthORM:
        pass


class PostgresUserAuthRepository(IUserAuthRepository):
    def get_by_phone_number(self, phone_number: str) -> UserAuthORM | None:
        try:
            return UserAuthORM.objects.get(phone_number=phone_number)
        except UserAuthORM.DoesNotExist:
            return None

    def get_by_email(self, email: str) -> UserAuthORM | None:
        try:
            return UserAuthORM.objects.get(email=email)
        except UserAuthORM.DoesNotExist:
            return None

    def create(
        self, phone_number: str | None = None, email: str | None = None
    ) -> UserAuthORM:
        if phone_number:
            return UserAuthORM.objects.create(phone_number=phone_number)
        return UserAuthORM.objects.create(email=email)

    def update(self, user_auth: UserAuth) -> UserAuthORM:
        return UserAuthORM.objects.filter(oid=user_auth.oid).update(
            is_active=user_auth.is_active,
            token=user_auth.token,
            updated_at=user_auth.updated_at,
        )

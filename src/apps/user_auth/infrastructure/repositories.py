from abc import ABC, abstractmethod

from src.apps.user_auth.infrastructure.models import UserAuthORM


class IUserAuthRepository(ABC):
    @abstractmethod
    def get_by_phone_number(self, phone_number: str) -> UserAuthORM | None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> UserAuthORM | None:
        pass

    @abstractmethod
    def create(self, user_auth_orm: UserAuthORM) -> UserAuthORM:
        pass

    @abstractmethod
    def update(self, user_auth_orm: UserAuthORM) -> UserAuthORM:
        pass


class PostgresUserAuthRepository(IUserAuthRepository):
    def get_by_phone_number(self, phone_number: str) -> UserAuthORM | None:
        return UserAuthORM.objects.get(phone_number=phone_number)

    def get_by_email(self, email: str) -> UserAuthORM | None:
        return UserAuthORM.objects.get(email=email)

    def create(self, user_auth_orm: UserAuthORM) -> UserAuthORM:
        if user_auth_orm.phone_number:
            return UserAuthORM.objects.create(phone_number=user_auth_orm.phone_number)
        return UserAuthORM.objects.create(email=user_auth_orm.email)

    def update(self, user_auth_orm: UserAuthORM) -> UserAuthORM:
        return UserAuthORM.objects.filter(oid=user_auth_orm.oid).update(
            is_active=user_auth_orm.is_active, token=user_auth_orm.token
        )

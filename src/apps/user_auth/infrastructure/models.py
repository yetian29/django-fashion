from uuid import uuid4

from django.db import models

from src.apps.base.infrastructure.models import BaseOidORM, BaseTimeORM
from src.apps.user_auth.domain.entities import UserAuth

# Create your models here.


class UserAuthORM(BaseOidORM, BaseTimeORM):
    phone_number = models.CharField(max_length=10, null=True, default=None)
    email = models.CharField(max_length=32, null=True, default=None)
    token = models.UUIDField(null=True, default=None)
    is_active = models.BooleanField(default=False)

    @staticmethod
    def from_entity(entity: UserAuth) -> "UserAuthORM":
        if not entity.oid:
            entity.oid = uuid4()
        return UserAuthORM(
            oid=entity.oid,
            phone_number=entity.phone_number,
            email=entity.email,
            token=entity.token,
            is_active=entity.is_active,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    def to_entity(self) -> UserAuth:
        return UserAuth(
            oid=self.oid,
            phone_number=self.phone_number,
            email=self.email,
            token=self.token,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    class Meta:
        verbose_name = "UserAuthORM"

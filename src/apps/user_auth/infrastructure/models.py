from django.db import models

from src.apps.base.infrastructure.models import BaseOidORM, BaseTimeORM
from src.apps.user_auth.domain.entities import UserAuth

# Create your models here.


class UserAuthORM(BaseOidORM, BaseTimeORM):
    phone_number = models.CharField(max_length=10, blank=True, null=True, default=None)
    email = models.CharField(max_length=32, blank=True, null=True, default=None)
    token = models.UUIDField(null=True, blank=True, default=None)
    is_active = models.BooleanField(default=False)

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

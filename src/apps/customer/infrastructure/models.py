from django.db import models

from src.apps.base.infrastructure.models import BaseOidORM, BaseTimeORM
from src.apps.customer.domain.entities import Customer

# Create your models here.


class CustomerORM(BaseOidORM, BaseTimeORM):
    phone_number = models.CharField(max_length=10, blank=True, null=True, default="")
    email = models.CharField(max_length=32, blank=True, null=True, default="")
    token = models.UUIDField(null=True, blank=True, default=None)
    is_active = models.BooleanField(default=False)

    def to_entity(self) -> Customer:
        return Customer(
            oid=self.oid,
            phone_number=self.phone_number,
            email=self.email,
            token=self.token,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def __str__(self):
        key = self.phone_number if self.phone_number else self.email
        return key

    class Meta:
        verbose_name = "CustomerORM"

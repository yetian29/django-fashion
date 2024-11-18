from uuid import uuid4

from django.db import models

# Create your models here.


class BaseOidORM(models.Model):
    oid = models.UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)


class BaseTimeORM(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

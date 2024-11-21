from dataclasses import dataclass
from uuid import UUID

from src.apps.base.domain.entities import BaseOid, BaseTime


@dataclass
class UserAuth(BaseOid, BaseTime):
    phone_number: str
    email: str
    token: UUID
    is_active: bool

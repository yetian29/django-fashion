from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Customer:
    phone_number: str
    email: str
    oid: UUID | None = None
    token: UUID | None = None
    is_active: bool = False
    created_at: datetime | None = None
    updated_at: datetime | None = None

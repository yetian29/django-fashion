from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class BaseOid:
    oid: UUID


@dataclass(frozen=True)
class BaseTime:
    created_at: datetime
    updated_at: datetime

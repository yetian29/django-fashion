from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class BaseOid:
    oid: UUID


@dataclass
class BaseTime:
    created_at: datetime
    updated_at: datetime

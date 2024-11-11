from dataclasses import dataclass
from datetime import datetime


@dataclass
class BaseTime:
    created_at: datetime
    updated_at: datetime

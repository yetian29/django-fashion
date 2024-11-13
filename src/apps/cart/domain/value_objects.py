from enum import Enum


class CartStatusEnum(str, Enum):
    EMPTY = "EMPTY", "Empty Cart"
    NORMAL = "NORMAL", "Normal Cart"
    FULL = "FULL", "Full Cart"

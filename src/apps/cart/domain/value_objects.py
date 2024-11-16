from enum import Enum


class CartStatusEnum(str, Enum):
    EMPTY = "Empty Cart"
    NORMAL = "Normal Cart"
    FULL = "Full Cart"

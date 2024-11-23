from enum import Enum


class CartStatusEnum(str, Enum):
    EMPTY = "EMPTY CART"
    NORMAL = "NORMAL CART"
    FULL = "FULL CART"

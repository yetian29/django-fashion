from src.apps.base.domain.errors import BaseDomainException


class CartIsNotFoundException(BaseDomainException):
    pass


class QtyInvalidException(BaseDomainException):
    pass

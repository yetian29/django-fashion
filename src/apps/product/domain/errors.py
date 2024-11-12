from src.apps.base.domain.errors import BaseDomainException


class ProductIsNotFoundException(BaseDomainException):
    pass


class ProductsAreNotFoundException(BaseDomainException):
    pass

from src.apps.base.domain.errors import BaseDomainException


class CachedDataAreNotFoundException(BaseDomainException):
    pass


class CodeIsExpiredException(BaseDomainException):
    pass


class CodesAreNotEqualException(BaseDomainException):
    pass


class UserAuthIsNotFoundException(BaseDomainException):
    pass

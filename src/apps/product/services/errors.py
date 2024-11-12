from src.apps.base.helper.errors import BaseServiceException


class ProductIsNotFoundException(BaseServiceException):
    pass


class ProductsAreNotFoundException(BaseServiceException):
    pass

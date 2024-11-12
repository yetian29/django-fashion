def fail(exc: Exception):
    raise exc


class BaseServiceException(Exception):
    pass

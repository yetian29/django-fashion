from functools import lru_cache

import punq

from src.apps.product.domain.services import IProductService
from src.apps.product.domain.use_cases import GetProductListUseCase, GetProductUseCase
from src.apps.product.infrastructure.repositories import (
    IProductRepository,
    PostgresProductRepository,
)
from src.apps.product.services.products import ProductService
from src.apps.user_auth.domain.services import (
    ICodeService,
    ILoginService,
    ISendCodeService,
    IUserAuthService,
)
from src.apps.user_auth.domain.use_cases import (
    AuthorizeUserAuthUseCase,
    LoginUserAuthUseCase,
)
from src.apps.user_auth.infrastructure.repositories import (
    IUserAuthRepository,
    PostgresUserAuthRepository,
)
from src.apps.user_auth.services.user_auth import (
    CodeService,
    LoginService,
    SendCodeService,
    UserAuthService,
)


@lru_cache(1)
def get_container() -> punq.Container:
    return init_container()


def init_container() -> punq.Container:
    container = punq.Container()

    container.register(IUserAuthRepository, PostgresUserAuthRepository)
    container.register(ICodeService, CodeService)
    container.register(ISendCodeService, SendCodeService)
    container.register(ILoginService, LoginService)
    container.register(IUserAuthService, UserAuthService)
    container.register(AuthorizeUserAuthUseCase)
    container.register(LoginUserAuthUseCase)

    container.register(IProductRepository, PostgresProductRepository)
    container.register(IProductService, ProductService)
    container.register(GetProductUseCase)
    container.register(GetProductListUseCase)

    return container

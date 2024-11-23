from functools import lru_cache

import punq

from src.apps.customer.domain.services import (
    ICodeService,
    ICustomerService,
    ILoginService,
    ISendCodeService,
)
from src.apps.customer.domain.use_cases import (
    AuthorizeCustomerUseCase,
    LoginCustomerUseCase,
)
from src.apps.customer.infrastructure.repositories import (
    ICustomerRepository,
    PostgresCustomerRepository,
)
from src.apps.customer.services.customer import (
    CodeService,
    CustomerService,
    LoginService,
    SendCodeService,
)
from src.apps.product.domain.services import IProductService
from src.apps.product.domain.use_cases import GetProductListUseCase, GetProductUseCase
from src.apps.product.infrastructure.repositories import (
    IProductRepository,
    PostgresProductRepository,
)
from src.apps.product.services.products import ProductService


@lru_cache(1)
def get_container() -> punq.Container:
    return init_container()


def init_container() -> punq.Container:
    container = punq.Container()

    container.register(ICustomerRepository, PostgresCustomerRepository)
    container.register(ICodeService, CodeService)
    container.register(ISendCodeService, SendCodeService)
    container.register(ILoginService, LoginService)
    container.register(ICustomerService, CustomerService)
    container.register(AuthorizeCustomerUseCase)
    container.register(LoginCustomerUseCase)

    container.register(IProductRepository, PostgresProductRepository)
    container.register(IProductService, ProductService)
    container.register(GetProductUseCase)
    container.register(GetProductListUseCase)

    return container

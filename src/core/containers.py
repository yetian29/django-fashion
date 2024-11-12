from functools import lru_cache

import punq

from apps.product.domain.services import IProductService
from apps.product.domain.use_cases import GetProductListUseCase, GetProductUseCase
from apps.product.infrastructure.repositories import (
    IProductRepository,
    PostgresProductRepository,
)
from apps.product.services.products import ProductService


@lru_cache(1)
def get_container() -> punq.Container:
    return init_container()

def init_container() -> punq.Container:
    container = punq.Container()

    # Register Dependencies Of Product
    container.register(IProductRepository, PostgresProductRepository)
    container.register(IProductService, ProductService)
    container.register(GetProductUseCase)
    container.register(GetProductListUseCase)

    return container

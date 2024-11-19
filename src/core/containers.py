import punq

from src.apps.product.domain.services import IProductService
from src.apps.product.domain.use_cases import GetProductListUseCase, GetProductUseCase
from src.apps.product.infrastructure.repositories import (
    IProductRepository,
    PostgresProductRepository,
)
from src.apps.product.services.products import ProductService


def init_container() -> punq.Container:
    container = punq.Container()

    container.register(IProductRepository, PostgresProductRepository)
    container.register(IProductService, ProductService)
    container.register(GetProductUseCase)
    container.register(GetProductListUseCase)

    return container

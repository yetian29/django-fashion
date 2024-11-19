import punq
import pytest

from src.apps.product.domain.services import IProductService
from src.apps.product.domain.use_cases import GetProductListUseCase, GetProductUseCase
from test.mock.service.product import DummyProductService


@pytest.fixture
def mock_test_container() -> punq.Container:
    container = punq.Container()

    container.register(IProductService, DummyProductService)
    container.register(GetProductUseCase)
    container.register(GetProductListUseCase)

    return container

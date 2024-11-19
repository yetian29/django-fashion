import pytest

from src.apps.product.domain.commands import GetProductListCommand
from src.apps.product.domain.use_cases import GetProductListUseCase, GetProductUseCase
from test.mock.factory.product import GetProductCommandFactory


@pytest.fixture
def mock_test_get_product_use_case(mock_test_container):
    return mock_test_container.resolve(GetProductUseCase)


@pytest.fixture
def mock_test_get_product_list_use_case(mock_test_container):
    return mock_test_container.resolve(GetProductListUseCase)


def test_get_product_use_case(mock_test_get_product_use_case):
    command = GetProductCommandFactory.build()
    product = mock_test_get_product_use_case.execute(command)
    assert product.oid == command.oid


def test_get_product_list_use_case(mock_test_get_product_list_use_case):
    command = GetProductListCommand()
    products, count = mock_test_get_product_list_use_case.execute(command)
    assert len(products) <= command.pagination.limit
    assert count <= 1000

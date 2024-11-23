import punq
import pytest

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
from src.apps.product.domain.services import IProductService
from src.apps.product.domain.use_cases import GetProductListUseCase, GetProductUseCase
from test.mock.service.customer import (
    DummyCodeService,
    DummyCustomerService,
    DummyLoginService,
    DummySendCodeService,
)
from test.mock.service.product import DummyProductService


@pytest.fixture
def mock_test_container() -> punq.Container:
    container = punq.Container()

    container.register(ICodeService, DummyCodeService, scope=punq.Scope.singleton)
    container.register(ISendCodeService, DummySendCodeService)
    container.register(ILoginService, DummyLoginService)
    container.register(ICustomerService, DummyCustomerService)
    container.register(AuthorizeCustomerUseCase)
    container.register(LoginCustomerUseCase)

    container.register(IProductService, DummyProductService)
    container.register(GetProductUseCase)
    container.register(GetProductListUseCase)

    return container

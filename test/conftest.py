import punq
import pytest

from src.apps.product.domain.services import IProductService
from src.apps.product.domain.use_cases import GetProductListUseCase, GetProductUseCase
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
from test.mock.service.product import DummyProductService
from test.mock.service.user_auth import (
    DummyCodeService,
    DummyLoginService,
    DummySendCodeService,
    DummyUserAuthService,
)


@pytest.fixture
def mock_test_container() -> punq.Container:
    container = punq.Container()

    container.register(ICodeService, DummyCodeService, scope=punq.Scope.singleton)
    container.register(ISendCodeService, DummySendCodeService)
    container.register(ILoginService, DummyLoginService)
    container.register(IUserAuthService, DummyUserAuthService)
    container.register(AuthorizeUserAuthUseCase)
    container.register(LoginUserAuthUseCase)

    container.register(IProductService, DummyProductService)
    container.register(GetProductUseCase)
    container.register(GetProductListUseCase)

    return container

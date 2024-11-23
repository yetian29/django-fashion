from uuid import UUID

import pytest

from src.apps.customer.domain.use_cases import (
    AuthorizeCustomerUseCase,
    LoginCustomerUseCase,
)
from test.mock.factory.customer import (
    AuthorizeCustomerCommandFactory,
    LoginCustomerCommandFactory,
)


@pytest.fixture
def mock_test_authorize_customer_use_case(
    mock_test_container,
) -> AuthorizeCustomerUseCase:
    return mock_test_container.resolve(AuthorizeCustomerUseCase)


@pytest.fixture
def mock_test_login_customer_use_case(mock_test_container) -> LoginCustomerUseCase:
    return mock_test_container.resolve(LoginCustomerUseCase)


def test_authorize_and_login_customer_use_case(
    mock_test_authorize_customer_use_case, mock_test_login_customer_use_case
):
    command1 = AuthorizeCustomerCommandFactory.build()
    code = mock_test_authorize_customer_use_case.execute(command1)
    command2 = LoginCustomerCommandFactory.build(
        phone_number=command1.customer.phone_number,
        email=command1.customer.email,
        code=code,
    )
    token = mock_test_login_customer_use_case.execute(command2)
    assert len(code) == 6
    assert code.isdigit()
    assert UUID(str(token), version=4)

from uuid import UUID

import pytest

from src.apps.user_auth.domain.use_cases import (
    AuthorizeUserAuthUseCase,
    LoginUserAuthUseCase,
)
from test.mock.factory.user_auth import (
    AuthorizeUserAuthCommandFactory,
    LoginUserAuthCommandFactory,
)


@pytest.fixture
def mock_test_authorize_user_auth_use_case(
    mock_test_container,
) -> AuthorizeUserAuthUseCase:
    return mock_test_container.resolve(AuthorizeUserAuthUseCase)


@pytest.fixture
def mock_test_login_user_auth_use_case(mock_test_container) -> LoginUserAuthUseCase:
    return mock_test_container.resolve(LoginUserAuthUseCase)


def test_authorize_and_login_user_auth_use_case(
    mock_test_authorize_user_auth_use_case, mock_test_login_user_auth_use_case
):
    command1 = AuthorizeUserAuthCommandFactory.build()
    code = mock_test_authorize_user_auth_use_case.execute(command1)
    command2 = LoginUserAuthCommandFactory.build(
        phone_number=command1.user_auth.phone_number,
        email=command1.user_auth.email,
        code=code,
    )
    token = mock_test_login_user_auth_use_case.execute(command2)
    assert len(code) == 6
    assert code.isdigit()
    assert UUID(str(token), version=4)

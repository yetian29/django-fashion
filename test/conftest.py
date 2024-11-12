import punq
import pytest


@pytest.fixture(scope="session")
def mock_test_container() -> punq.Container:
    container = punq.Container()
    return container

import pytest


@pytest.fixture()
def five() -> int:
    return 5


@pytest.fixture(scope="session")
def create_test_db() -> None:
    ...


# @pytest.fixture(scope="function")
# def async_session() -> AsyncSession:
#     ...


@pytest.fixture(scope="function", autouse=True)
def clear_test_db() -> None:
    ...

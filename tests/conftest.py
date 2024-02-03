# Active pytester plugin (https://docs.pytest.org/en/7.1.x/how-to/writing_plugins.html#testing-plugins)
from pathlib import Path

import pytest
from pytest_lock import FixtureLock
from pytest_lock.plugin import _lock

pytest_plugins = ["pytester"]


@pytest.fixture(scope="function")
def lock_test(pytestconfig: pytest.Config, request: pytest.FixtureRequest) -> FixtureLock:
    """
    Fixture to give access to lock feature.

    Note:
        Without this manipulation, the plugin don't work if we want to test it.

    Args:
        pytestconfig (Config): Pytest configuration.
        request (FixtureRequest): Pytest request.

    Returns:
        FixtureLock: Lock fixture.
    """
    # Use pytestconfig and request of test function
    env_tests_path = Path(__name__).parent.absolute()

    # Use default values of plugin
    from pytest_lock.plugin import CACHE_LOCK_PATH, EXTENSION
    env_cache_lock_path = env_tests_path / CACHE_LOCK_PATH
    extension = EXTENSION

    lock_fixture = _lock(  # noqa: F841
        pytestconfig=pytestconfig,
        request=request,
        tests_path=env_tests_path,
        cache_path=env_cache_lock_path,
        extension=extension,
    )

    yield lock_fixture

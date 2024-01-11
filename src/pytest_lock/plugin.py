"""
Entry point of pytest-lock plugin.

Pytest will automatically load this file when the plugin is activated.
Pytest will use the function 'pytest_addoption' to add new argument CLI.
Pytest will use the fixture 'lock' to give access to the lock feature.
"""

import pytest
from _pytest.config import Config
from pytest import FixtureRequest

from pytest_lock import PROJECT_PATH
from pytest_lock.core.cache import CacheLock
from pytest_lock.core.config import ArgumentCLI, LockConfig
from pytest_lock.core.fixture import FixtureLock
from pytest_lock.core.parser_file.builder import ParserFileBuilder

CACHE_LOCK_PATH = PROJECT_PATH / ".pytest_lock"
TESTS_PATH = PROJECT_PATH / "tests"
EXTENSION = ".json"


def pytest_addoption(parser: Config):
    """Add new argument CLI to pytest."""

    parser.addoption(ArgumentCLI.LOCK, action="store_true", help="Activate lock feature")  # type: ignore
    parser.addoption(ArgumentCLI.SIMULATE, action="store_true", help="Simulate lock feature")  # type: ignore
    parser.addoption(ArgumentCLI.LOCK_DATE, action="store", type=str, help="Activate lock date feature")  # type: ignore
    parser.addoption(ArgumentCLI.REVERSED, action="store_true", help="Activate reversed feature")  # type: ignore
    parser.addoption(ArgumentCLI.ONLY_SKIP, action="store_true", help="Lock only tests without lock")  # type: ignore


@pytest.fixture(scope="function")
def lock(pytestconfig: Config, request: FixtureRequest) -> FixtureLock:
    """
    Fixture to give access to lock feature.

    This fixture is used to give access to lock feature.
    Pytest will automatically load this fixture when the plugin is activated.
    """
    config = LockConfig(
        pytestconfig,
        request,
        extension=EXTENSION,
        tests_path=TESTS_PATH,
        cache_path=CACHE_LOCK_PATH,
    )

    parser_file_builder = ParserFileBuilder()
    parser_file = parser_file_builder.build(EXTENSION)
    cache_system = CacheLock(config, parser_file)

    lock_fixture = FixtureLock(config, cache_system)
    return lock_fixture

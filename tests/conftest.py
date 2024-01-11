# Active pytester plugin (https://docs.pytest.org/en/7.1.x/how-to/writing_plugins.html#testing-plugins)
from pathlib import Path

import pytest
from pytest_lock import FixtureLock
from pytest_lock.core.cache import CacheLock
from pytest_lock.core.config import LockConfig
from pytest_lock.core.parser_file.builder import ParserFileBuilder

pytest_plugins = ["pytester"]


@pytest.fixture(scope="function")
def lock_test(pytestconfig: pytest.Config, request: pytest.FixtureRequest) -> FixtureLock:
    ENV_TESTS_PATH = Path(__name__).parent.absolute()
    ENV_CACHE_LOCK_PATH = ENV_TESTS_PATH / ".pytest_lock"
    EXTENSION = ".json"

    config = LockConfig(pytestconfig, request, extension=EXTENSION, tests_path=ENV_TESTS_PATH, cache_path=ENV_CACHE_LOCK_PATH)

    parser_file_builder = ParserFileBuilder()
    parser_file = parser_file_builder.build(EXTENSION)
    cache_system = CacheLock(config, parser_file)

    lock_fixture = FixtureLock(config, cache_system)

    yield lock_fixture

    # Delete cache file

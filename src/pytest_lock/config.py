from pathlib import Path

import pytest
from _pytest.config import Config

from pytest_lock.__globals__ import CACHE_LOCK_PATH, TESTS_PATH
from pytest_lock.models.cli_argument import ArgumentCLI


class LockConfig:
    cache_path: Path

    is_lock: bool
    is_simulate: bool
    is_lock_date: bool
    is_reversed: bool
    only_skip: bool

    def __init__(
        self,
        pytestconfig: Config,
        request: pytest.FixtureRequest,
        extension: str = ".json",
        date_format: str = "%Y-%m-%d",
    ):
        file_path = request.path
        relative_path = file_path.relative_to(TESTS_PATH)
        relative_path = relative_path.with_suffix(extension)

        self.extension = extension
        self.date_format = date_format
        self.cache_path = CACHE_LOCK_PATH / relative_path.as_posix()

        self.is_lock = pytestconfig.getoption(ArgumentCLI.LOCK)
        self.is_simulate = pytestconfig.getoption(ArgumentCLI.SIMULATE)
        self.is_lock_date = pytestconfig.getoption(ArgumentCLI.LOCK_DATE)
        self.is_reversed = pytestconfig.getoption(ArgumentCLI.REVERSED)
        self.only_skip = pytestconfig.getoption(ArgumentCLI.ONLY_SKIP)

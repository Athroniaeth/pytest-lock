from pathlib import Path

import pytest
from _pytest.config import Config

from pytest_lock.models.cli_argument import ArgumentCLI
from pytest_lock.models.exceptions import LockCLIException


class LockConfig:
    cache_path: Path

    is_lock: bool
    is_simulate: bool
    is_lock_date: str
    is_reversed: bool
    only_skip: bool

    def __init__(
        self,
        pytestconfig: Config,
        request: pytest.FixtureRequest,
        tests_path: Path,
        cache_path: Path,
        extension: str = ".json",
        date_format: str = "%Y/%m/%d",
    ):
        file_path = request.path
        relative_path = file_path.relative_to(tests_path)
        relative_path = relative_path.with_suffix(extension)

        self.extension = extension
        self.date_format = date_format
        self.cache_path = cache_path / "cache" / relative_path.as_posix()

        self.is_lock = pytestconfig.getoption(ArgumentCLI.LOCK)
        self.is_simulate = pytestconfig.getoption(ArgumentCLI.SIMULATE)
        self.is_lock_date = pytestconfig.getoption(ArgumentCLI.LOCK_DATE)
        self.is_reversed = pytestconfig.getoption(ArgumentCLI.REVERSED)
        self.only_skip = pytestconfig.getoption(ArgumentCLI.ONLY_SKIP)

        if not self.is_lock:
            if self.is_simulate:
                raise LockCLIException("Can't activate '--simulate' mode without '--lock'")
            if self.is_lock_date:
                raise LockCLIException(f"Can't activate '--lock-date', '{self.is_lock_date}' mode without '--lock'")
            if self.only_skip:
                raise LockCLIException("Can't activate '--only-skip' mode without '--lock'")

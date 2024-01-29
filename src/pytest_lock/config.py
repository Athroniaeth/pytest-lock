from dataclasses import dataclass
from pathlib import Path

import pytest
from _pytest.config import Config

from pytest_lock.models.cli_argument import ArgumentCLI
from pytest_lock.models.exceptions import LockCLIException


@dataclass
class LockConfig:
    """
    Configuration for Lock fixture.

    Args:
        tests_path: Path of tests
        cache_path: Path of cache file
        file_path: Path of current test

        is_lock: Activate lock system
        is_simulate: Activate simulate mode
        is_lock_date: Activate lock date
        only_skip: Activate only skip mode

        extension: Extension of cache file
        date_format: Format of date in cache file

    """

    tests_path: Path
    cache_path: Path
    file_path: Path

    is_lock: bool
    is_simulate: bool
    is_lock_date: str
    only_skip: bool

    extension: str
    date_format: str

    @classmethod
    def from_pytest_run(
        cls,
        pytestconfig: Config,
        request: pytest.FixtureRequest,
        tests_path: Path,
        cache_path: Path,
        extension: str,
        date_format: str = "%Y/%m/%d",
    ) -> "LockConfig":
        """
        Create a LockConfig from pytest run

        Args:
            pytestconfig: Config of pytest
            request: Request of pytest
            tests_path: Path of tests
            cache_path: Path of cache
            extension: Extension of cache file
            date_format: Format of date in cache file

        Returns:
            LockConfig from pytest run
        """

        is_lock = pytestconfig.getoption(ArgumentCLI.LOCK)
        is_simulate = pytestconfig.getoption(ArgumentCLI.SIMULATE)
        is_lock_date = pytestconfig.getoption(ArgumentCLI.LOCK_DATE)
        only_skip = pytestconfig.getoption(ArgumentCLI.ONLY_SKIP)

        if not is_lock:
            if is_simulate:
                raise LockCLIException("Can't activate '--simulate' mode without '--lock'")
            if is_lock_date:
                raise LockCLIException(f"Can't activate '--lock-date', '{is_lock_date}' mode without '--lock'")
            if only_skip:
                raise LockCLIException("Can't activate '--only-skip' mode without '--lock'")

        return cls(
            tests_path=tests_path,
            cache_path=cache_path,
            file_path=request.path,
            is_lock=is_lock,
            is_simulate=is_simulate,
            is_lock_date=is_lock_date,
            only_skip=only_skip,
            extension=extension,
            date_format=date_format,
        )

    def get_file_cache(self) -> Path:
        """
        Return the file cache of this test

        Notes:
            The extension can change, also need to actualize the path,
            The cache handler the change of file cache parser

        Returns:
            Path of cache file
        """
        relative_path = self.file_path.relative_to(self.tests_path)
        relative_path = relative_path.with_suffix(self.extension)

        cache_path = self.cache_path / "cache" / relative_path.as_posix()
        return cache_path

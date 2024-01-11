from typing import List

import pytest
from _pytest.pytester import Pytester
from pytest_lock.models.exceptions import LockCLIException


@pytest.mark.parametrize(
    "arguments",
    [
        ["--simulate"],  # Can't simulate without --lock
        ["--lock-date", "2000/01/01"],  # Can't lock-date without --lock
        ["--only-skip"],  # Can't 'only-skip' without --lock
    ],
)
def test_bad_arguments(pytester: Pytester, arguments: List[str]):
    pytester.copy_example("conftest.py")
    pytester.copy_example("scenarios/test_classic_lock.py")

    result = pytester.runpytest(*arguments)
    result.assert_outcomes(errors=1)

    cli_arguments_str = ", ".join([f"'{arg}'" for arg in arguments])
    exception = LockCLIException(f"Can't activate {cli_arguments_str} mode without '--lock'")
    assert f"{exception}" in result.stdout.str()


@pytest.mark.parametrize(
    "arguments",
    [
        ["--lock"],
        ["--lock", "--simulate"],
        ["--lock", "--lock-date", "2000/01/01"],
        ["--lock", "--only-skip"],
    ],
)
def test_good_arguments(pytester: Pytester, arguments: List[str]):
    pytester.copy_example("conftest.py")
    pytester.copy_example("scenarios/test_classic_lock.py")

    result = pytester.runpytest(*arguments)

    result.assert_outcomes(passed=1)

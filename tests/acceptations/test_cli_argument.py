from typing import List

import pytest
from _pytest.pytester import Pytester

from pytest_lock.models.cli_argument import ArgumentCLI
from pytest_lock.models.exceptions import LockCLIException


@pytest.mark.parametrize(
    ("argument_cli", "argument_cli_old"),
    [
        (ArgumentCLI.LOCK, "--lock"),
        (ArgumentCLI.LOCK_DATE, "--lock-date"),
        (ArgumentCLI.ONLY_SKIP, "--only-skip"),
        (ArgumentCLI.SIMULATE, "--simulate"),
        (ArgumentCLI.CLEAN, "--clean"),
    ],
)
def test_same_arguments(argument_cli: str, argument_cli_old: str):
    """ Check that ArgumentCLI still has the same commands as previously determined. """
    assert argument_cli == argument_cli_old


@pytest.mark.parametrize(
    "arguments",
    [
        [ArgumentCLI.CLEAN],  # Can't clean without --lock
        [ArgumentCLI.SIMULATE],  # Can't simulate without --lock
        [ArgumentCLI.ONLY_SKIP],  # Can't 'only-skip' without --lock
        [ArgumentCLI.LOCK_DATE, "2000/01/01"],  # Can't lock-date without --lock
    ],
)
def test_bad_arguments(pytester: Pytester, arguments: List[str]):
    pytester.copy_example("conftest.py")
    pytester.copy_example("scenarios/test_fixture_call.py")

    result = pytester.runpytest(*arguments)
    result.assert_outcomes(errors=1)

    cli_arguments_str = ", ".join([f"'{arg}'" for arg in arguments])
    exception = LockCLIException(f"Can't activate {cli_arguments_str} mode without '{ArgumentCLI.LOCK}'")
    assert f"{exception}" in result.stdout.str()


@pytest.mark.parametrize(
    "arguments",
    [
        [ArgumentCLI.LOCK],
        [ArgumentCLI.LOCK, ArgumentCLI.CLEAN],
        [ArgumentCLI.LOCK, ArgumentCLI.SIMULATE],
        [ArgumentCLI.LOCK, ArgumentCLI.ONLY_SKIP],
        [ArgumentCLI.LOCK, ArgumentCLI.LOCK_DATE, "2000/01/01"],
    ],
)
def test_good_arguments(pytester: Pytester, arguments: List[str]):
    pytester.copy_example("conftest.py")
    pytester.copy_example("scenarios/test_fixture_call.py")

    result = pytester.runpytest(*arguments)

    result.assert_outcomes(passed=1)

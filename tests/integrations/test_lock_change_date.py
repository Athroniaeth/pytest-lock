import datetime

from _pytest.pytester import Pytester

from pytest_lock.models.cli_argument import ArgumentCLI
from pytest_lock.parser_file.builder import ParserFileBuilder

number_extension = ParserFileBuilder().mapping.keys().__len__()
number_tests = 8 * number_extension  # Each test is repeated for each extension


def test_lock_change_date_today(pytester: Pytester) -> None:
    """Test the creation of a cache."""
    today = datetime.date.today()
    today = today.strftime("%Y/%m/%d")

    pytester.copy_example("conftest.py")
    pytester.copy_example("scenarios/test_fixture_lock_diversified.py")

    result = pytester.runpytest(ArgumentCLI.LOCK, ArgumentCLI.LOCK_DATE, f"{today}")
    result.assert_outcomes(passed=number_tests)

    result = pytester.runpytest()
    result.assert_outcomes(passed=number_tests)


def test_lock_change_date_yesterday(pytester: Pytester) -> None:
    """Test the creation of a cache."""
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    yesterday = yesterday.strftime("%Y/%m/%d")

    pytester.copy_example("conftest.py")
    pytester.copy_example("scenarios/test_fixture_lock_diversified.py")

    result = pytester.runpytest(ArgumentCLI.LOCK, ArgumentCLI.LOCK_DATE, f"{yesterday}")
    result.assert_outcomes(passed=number_tests)

    result = pytester.runpytest()
    result.assert_outcomes(failed=number_tests)


def test_lock_change_date_tomorrow(pytester: Pytester) -> None:
    """Test the creation of a cache."""
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow = tomorrow.strftime("%Y/%m/%d")

    pytester.copy_example("conftest.py")
    pytester.copy_example("scenarios/test_fixture_lock_diversified.py")

    result = pytester.runpytest(ArgumentCLI.LOCK, ArgumentCLI.LOCK_DATE, f"{tomorrow}")
    result.assert_outcomes(passed=number_tests)

    result = pytester.runpytest()
    result.assert_outcomes(passed=number_tests)

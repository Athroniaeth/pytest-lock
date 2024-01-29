import datetime

from _pytest.pytester import Pytester

from pytest_lock.models.cli_argument import ArgumentCLI


def test_lock_change_date_today(pytester: Pytester) -> None:
    """Test the creation of a cache."""
    today = datetime.date.today()
    today = today.strftime("%Y/%m/%d")

    pytester.copy_example("conftest.py")
    pytester.copy_example("scenarios/test_fixture_lock.py")

    result = pytester.runpytest(ArgumentCLI.LOCK, ArgumentCLI.LOCK_DATE, f"{today}")
    result.assert_outcomes(skipped=1)

    result = pytester.runpytest()
    result.assert_outcomes(passed=1)


def test_lock_change_date_yesterday(pytester: Pytester) -> None:
    """Test the creation of a cache."""
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    yesterday = yesterday.strftime("%Y/%m/%d")

    pytester.copy_example("conftest.py")
    pytester.copy_example("scenarios/test_fixture_lock.py")

    result = pytester.runpytest(ArgumentCLI.LOCK, ArgumentCLI.LOCK_DATE, f"{yesterday}")
    result.assert_outcomes(skipped=1)

    result = pytester.runpytest()
    result.assert_outcomes(failed=1)


def test_lock_change_date_tomorrow(pytester: Pytester) -> None:
    """Test the creation of a cache."""
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow = tomorrow.strftime("%Y/%m/%d")

    pytester.copy_example("conftest.py")
    pytester.copy_example("scenarios/test_fixture_lock.py")

    result = pytester.runpytest(ArgumentCLI.LOCK, ArgumentCLI.LOCK_DATE, f"{tomorrow}")
    result.assert_outcomes(skipped=1)

    result = pytester.runpytest()
    result.assert_outcomes(passed=1)

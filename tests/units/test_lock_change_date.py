import datetime

from _pytest.pytester import Pytester


def test_lock_change_date_today(pytester: Pytester) -> None:
    """Test the creation of a cache."""
    today = datetime.date.today()
    today = today.strftime("%Y/%m/%d")

    pytester.copy_example("conftest.py")
    pytester.copy_example("scenarios/test_classic_lock_call.py")

    result = pytester.runpytest(*["--lock", "--lock-date", f"{today}"])
    result.assert_outcomes(skipped=1)

    result = pytester.runpytest()
    result.assert_outcomes(passed=1)


def test_lock_change_date_yesterday(pytester: Pytester) -> None:
    """Test the creation of a cache."""
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    yesterday = yesterday.strftime("%Y/%m/%d")

    pytester.copy_example("conftest.py")
    pytester.copy_example("scenarios/test_classic_lock_call.py")

    result = pytester.runpytest(*["--lock", "--lock-date", f"{yesterday}"])
    result.assert_outcomes(skipped=1)

    result = pytester.runpytest()
    result.assert_outcomes(failed=1)


def test_lock_change_date_tomorrow(pytester: Pytester) -> None:
    """Test the creation of a cache."""
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow = tomorrow.strftime("%Y/%m/%d")

    pytester.copy_example("conftest.py")
    pytester.copy_example("scenarios/test_classic_lock_call.py")

    result = pytester.runpytest(*["--lock", "--lock-date", f"{tomorrow}"])
    result.assert_outcomes(skipped=1)

    result = pytester.runpytest()
    result.assert_outcomes(passed=1)

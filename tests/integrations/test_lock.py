from _pytest.pytester import Pytester

from pytest_lock.models.cli_argument import ArgumentCLI


def test_lock_diversified(pytester: Pytester) -> None:
    """Test scenario representing a "classic" pytest_lock test which will be used in Pytester"""
    pytester.copy_example("conftest.py")
    old_test_path = pytester.copy_example("scenarios/test_fixture_lock_diversified.py")

    result = pytester.runpytest(ArgumentCLI.LOCK)
    result.assert_outcomes(skipped=8)

    result = pytester.runpytest()
    result.assert_outcomes(passed=8)

from _pytest.pytester import Pytester

from pytest_lock.models.cli_argument import ArgumentCLI


def test_lock_change_result(pytester: Pytester) -> None:
    """Test the creation of a cache."""
    pytester.copy_example("conftest.py")
    old_test_path = pytester.copy_example("scenarios/lock_change_result/test_step_1.py")

    result = pytester.runpytest(ArgumentCLI.LOCK)
    result.assert_outcomes(passed=1)

    # Now the test is lock, change with test_step_2.py and run pytest again
    new_test_path = pytester.copy_example("scenarios/lock_change_result/test_step_2.py")
    old_test_path.unlink()
    new_test_path.rename(old_test_path)

    result = pytester.runpytest()
    result.assert_outcomes(failed=1)


def test_lock_change_result_type(pytester: Pytester) -> None:
    """Test the creation of a cache."""
    pytester.copy_example("conftest.py")
    old_test_path = pytester.copy_example("scenarios/lock_change_result_type/test_step_1.py")

    result = pytester.runpytest(ArgumentCLI.LOCK)
    result.assert_outcomes(passed=1)

    # Now the test is lock, change with test_step_2.py and run pytest again
    new_test_path = pytester.copy_example("scenarios/lock_change_result_type/test_step_2.py")
    old_test_path.unlink()
    new_test_path.rename(old_test_path)

    result = pytester.runpytest()
    result.assert_outcomes(failed=1)

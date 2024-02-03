from _pytest.pytester import Pytester

from pytest_lock.models.cli_argument import ArgumentCLI
from pytest_lock.parser_file.builder import ParserFileBuilder

number_extension = ParserFileBuilder().mapping.keys().__len__()
number_tests = 8 * number_extension  # Each test is repeated for each extension


def test_lock_diversified(pytester: Pytester) -> None:
    """Test scenario representing a "classic" pytest_lock test which will be used in Pytester"""

    pytester.copy_example("conftest.py")
    old_test_path = pytester.copy_example("scenarios/test_fixture_lock_diversified.py")

    # Todo : Check that the cache is writing 2 separate files

    result = pytester.runpytest(ArgumentCLI.LOCK)
    result.assert_outcomes(passed=number_tests)

    result = pytester.runpytest()
    result.assert_outcomes(passed=number_tests)

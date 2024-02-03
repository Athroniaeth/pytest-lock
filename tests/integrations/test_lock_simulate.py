from _pytest.pytester import Pytester

from pytest_lock.models.cli_argument import ArgumentCLI
from pytest_lock.parser_file.builder import ParserFileBuilder

number_extension = ParserFileBuilder().mapping.keys().__len__()
number_tests = 8 * number_extension  # Each test is repeated for each extension


def test_lock_change_date_today(pytester: Pytester) -> None:
    """Test the creation of a cache."""
    pytester.copy_example("conftest.py")
    pytester.copy_example("scenarios/test_fixture_lock_diversified.py")

    result = pytester.runpytest(ArgumentCLI.LOCK, ArgumentCLI.SIMULATE)

    result.assert_outcomes(passed=number_tests)

    # Check if the lock is simulated (not created)
    path_cache = pytester.path / ".pytest_cache" / "cache" / "test_fixture_lock_diversified.py"
    assert not path_cache.exists()

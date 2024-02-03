from _pytest.pytester import Pytester

from pytest_lock.models.cli_argument import ArgumentCLI


def test_default_values():
    """Test the default values of plugin file"""

    try:
        from pytest_lock.plugin import EXTENSION, TESTS_PATH, CACHE_LOCK_PATH
    except ImportError:
        assert False

    assert EXTENSION == ".pickle"
    assert TESTS_PATH == "tests"
    assert CACHE_LOCK_PATH == ".pytest_lock/cache"


def test_default_extension(pytester: Pytester):
    """
    Test the creation of a cache with the default extension.

    Notes:
        Allows you to see, regardless of the default value, that
        a lock with no indicated extension creates a .pickle file.
    Args:
        pytester:

    Returns:

    """
    pytester.copy_example("conftest.py")
    pytester.copy_example("scenarios/test_fixture_lock.py")

    result = pytester.runpytest(ArgumentCLI.LOCK)

    # Check if file with '.pickle' extension was create
    assert (pytester.path / ".pytest_lock" / "cache" / "test_fixture_lock.pickle").exists()

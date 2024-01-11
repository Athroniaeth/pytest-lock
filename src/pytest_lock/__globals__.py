from pytest_lock import PROJECT_PATH

# Variables useful for pytest-lock
CACHE_LOCK_PATH = PROJECT_PATH / ".pytest_lock" / "cache"
TESTS_PATH = PROJECT_PATH / "tests"
EXTENSION = ".json"

from pathlib import Path

from pytest_lock.core.fixture import FixtureLock

# Classic global variables
PROJECT_PATH = Path(__file__).parents[2]
SOURCE_PATH = Path(__file__).parents[1]
APP_PATH = Path(__file__).parents[0]

__all__ = ["FixtureLock"]

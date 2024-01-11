from pytest_lock.models.exceptions import LockException

if __name__ == "__main__":
    raise LockException("pytest-lock don't have a cli. Please use 'pytest' instead.")

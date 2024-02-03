# Lock clean

## Resume
The idea is as follows: the idea is to have a command to delete all locked tests. This will delete all caches that still have an associated test using `fixture` lock. `--clean` will delete all locked tests, and you will be warned that the tests are no longer locked.

## Usage

### Create tests

Create a test file, use the __lock__ fixture, for example `test_sum.py` in the `tests` directory. Here's an example:

```python
from pytest_lock import FixtureLock


def test_lock_sum(lock: FixtureLock):
    args = [1, 2, 3]
    lock.lock(sum, (args,))
```

### Locking Tests
Run pytest with the `--lock` option to generate the lock files:

```bash
pytest --lock
```

This will generate Pickle files in a `.pytest-lock` directory, storing the results of the locked tests.

### Use clean

Simply run pytest with the `--clean` option to delete all locked tests:

```bash
pytest --lock --clean
```

The cache of your tests will be deleted and you will be warned that the tests are no longer locked.
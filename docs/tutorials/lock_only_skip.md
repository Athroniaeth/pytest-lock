# Lock only skip

## Resume
The idea is as follows: when you use the `lock.lock` fixture, you may want to keep the result of a valid function in cache, but not keep it for the long term (because you want to check function locks frequently, because the function will change soon, etc.). `--only-skip` lets you choose a expiry date for the lock. When the date is exceeded, the test will be invalid and you will be warned to recheck the test.

## Usage
Create a test file, use the __lock__ fixture, for example `test_sum.py` in the `tests` directory. Here's an example:

```python
from pytest_lock import FixtureLock


def test_lock_sum(lock: FixtureLock):
    lock.lock(sum, ([],))
```

### Locking Tests
Run pytest with the `--lock` option to generate the lock files:

```bash
pytest --lock
```

Add another locking in the same file for example:

```python
from pytest_lock import FixtureLock


def test_lock_sum(lock: FixtureLock):
    lock.lock(sum, ([],))
    
def test_lock_sum_2(lock: FixtureLock):
    lock.lock(sum, ([1, 2, 3],))
```

Run pytest with the `--lock` and `--only-skip` option to generate the lock files:

```bash
pytest --lock --lock-only-skip
```
The lock of `sum` with args `[]` will be skipped, but the lock of sum with args `[1, 2, 3]` will be locked.
This will generate JSON files in a `.pytest-lock` directory, storing the results of the locked tests.

### Running Tests

Simply run pytest as you normally would:

```bash
pytest
```
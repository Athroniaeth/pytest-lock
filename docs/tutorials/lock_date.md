# Lock date

## Resume
The idea is as follows: when you use the `lock.lock` fixture, you may want to keep the result of a valid function in cache, but not keep it for the long term (because you want to check function locks frequently, because the function will change soon, etc.). `--lock-date` lets you choose a peremption date for the lock. When the date is exceeded, the test will be invalid and you will be warned to recheck the test.

## Usage

### Create tests

Create a test file, use the __lock__ fixture, for example `test_sum.py` in the `tests` directory. Here's an example:

```python
from pytest_lock import FixtureLock


def test_lock_sum(lock: FixtureLock):
    lock.lock(sum, ([1, 2, 3],))
```

### Locking Tests
Run pytest with the `--lock` and `--lock-date DATE` option to generate the lock files:

```{Note}
The date format is actually `%Y/%m/%d` (ex: `2024/01/01`), this format is not changeable for the moment.
```

```bash
pytest --lock --lock-date 2024/01/01
```

This will generate JSON files in a `.pytest-lock` directory, storing the results of the locked tests.

### Running Tests

Simply run pytest as you normally would (the 2024/01/01)

```bash
pytest
```

Simply run pytest as you normally would (the 2024/01/02)

```bash
pytest
```
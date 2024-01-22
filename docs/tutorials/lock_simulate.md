# Lock simulate

## Resume
### What is it?
The idea is this, you want to use the `lock.lock` fixture to lock tests, but you're not sure what will change and maybe it will corrupt your locked tests. `--simulate` allows you to simulate the locking of tests and have the same display as if you were running a normal test, but the locked tests will remain unchanged, and no locked tests will be added to the cache system.
## Usage

### Create tests

Create a test file, use the __lock__ fixture, for example `test_sum.py` in the `tests` directory. Here's an example:

```{warning}
This argument does not return an output code equal to 0 in all cases, but writing (i.e. updating or adding test locks) is disabled.
```

```python
from pytest_lock import FixtureLock


def test_lock_sum(lock: FixtureLock):
    lock.lock(sum, ([1, 2, 3],))
```

### Locking Tests
Run pytest with the `--lock` and `--simulate` option to generate the lock files:

```bash
pytest --lock --simulate
```

This will not generate JSON files in a `.pytest-lock` directory and don't store the results of the locked tests.

### Running Tests

Simply run pytest as you normally would:

```bash
pytest
```
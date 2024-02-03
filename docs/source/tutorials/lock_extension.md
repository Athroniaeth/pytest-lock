# Lock tests extension

## Usage

You can choose the extension of the lock file, you just need to add `extension='json'` for example. The default extension is `pickle`. If you choose a extension using string like json, you must lock a function who return a json serializable object.

- `pickle` (default)
- `json` (must have StrSupport with `__str__` method)
### Create tests

Create a test file, use the __lock__ fixture, for example `test_sum.py` in the `tests` directory. Here's an example:

```python
from pytest_lock import FixtureLock


def test_lock_sum(lock: FixtureLock):
    args = [1, 2, 3]
    lock.lock(sum, (args,), extension='json')
```

### Locking Tests
Run pytest with the `--lock` option to generate the lock files:

```bash
pytest --lock
```

This will generate JSON files in a `.pytest-lock` directory, storing the results of the locked tests.

### Running Tests

Simply run pytest as you normally would:

```bash
pytest
```
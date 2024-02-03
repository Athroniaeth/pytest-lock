# Lock tests

## Resume
### What is it?
The idea is that, in some projects, when we're going to do unit tests. There's going to be a lot of frustrating situations where we're simply going to test that an application with X arguments delivers result Y. We have to execute the code ourselves to get the result, and copy and paste it stupidly for the most complicated results. 

It's complicated to industrialize these tests with `pytest.mark.parametrize` because the result is not the same and makes industrialization impossible or makes the parametrize arguments unreadable. The concept of locking tests is to be able to lock the result of a test in a cache file, and to be able to reuse it later.

## Usage

### Create tests

Create a test file, use the __lock__ fixture, for example `test_sum.py` in the `tests` directory. Here's an example:

```python
from pytest_lock import FixtureLock


def test_lock_sum(lock: FixtureLock):
    args = [1, 2, 3]
    lock.lock(sum, (args,))
```

You can choose the extension of the lock file, you just need to add argument `extension='json'` for example. The default extension is `pickle`. If you choose a extension using string like json, you must lock a function who return a json serializable object.

- `.pickle` _(default extension)_
- `.json` _(must have StrSupport with `__str__` method)_

```python
from pytest_lock import FixtureLock


def test_lock_sum(lock: FixtureLock):
    args = [1, 2, 3]
    lock.lock(sum, (args,), extension='.json')
```

### Locking Tests
Run pytest with the `--lock` option to generate the lock files:

```bash
pytest --lock
```

This will generate Pickle or JSON files in a `.pytest-lock/cache` directory, storing the results of the locked tests.

### Running Tests

Simply run pytest as you normally would:

```bash
pytest
```
# Roadmap

- [X] Add fixtures `lock`
- [X] Add fixtures method `lock.lock` to lock the result of a test to a cache file
    - [X] If test use `lock.lock` and result was not locked, pytest exception is raised
    - [X] If test use `lock.lock` result is in the cache file and is the same as the result of the test, test is valid
    - [X] If test use `lock.lock` result is in the cache file and is not the same as the result of the test, test is
      invalid
    - [X] If test use `lock.lock` and `--lock` in cli argument, then lock the result of the test to a cache file (Any
      result with __str__ method and Exception are supported)
- [ ] Add support for `pytest --lock --lock-date 13/12/2023`, if test has `lock` fixture, then lock the result of the
  test to a cache file with the date of the lock, if date was expired, then the test is skipped
- [ ] Add fixtures method `lock.reversal`
    - [ ] If test use `lock.reversed` and `--lock --reversed` argument, then argument 'reversed' is useless, throw an
      exception
    - [ ] If test has `lock.reversed` and `--reversed` argument
        - [ ] If the result was not locked the plugin will skip the test
        - [ ] If the result was locked the plugin will check the type of the arguments of lock, if the test have
          list[int] as argument, then the plugin will check if the test failed with list[str], str, int, float, etc...
          and if it's the case, the test is valid
- [ ] Add arguments for `lock.reversed` to specify type to check, additionally, replace, or replace_joined

## Examples to test

```py 
from pytest_lock import FixtureLock


def test_something(lock: FixtureLock):
    lock.lock(sum, [1, 2, 3])  # use the lock function to lock the result of the test
    ...


def test_something_2(lock: FixtureLock):
    lock.reversed(sum, [1, 2, 3])  # use the lock function to lock the result of the test
    ...
``` 

```bash
pytest
```

```bash
pytest --lock
```

```bash
pytest --lock --lock-date 13/12/2023
```

```bash
pytest --reversed
```

```bash
pytest --lock --reversed
```


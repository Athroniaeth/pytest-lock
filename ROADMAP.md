# Roadmap

## Introduction

### Lock tests

This idea came from the fact that in the projects I do, or in open source/corporate projects, we very often do unit
tests with low added value, that is, tests that verify that the result of a function is always the same. (Having already
written the function). The goal is to have a faster way to do these tests, and to be able to reuse/update them easily.
We will therefore be able to lock the tests, that is to say, to be able to verify that the result of a test is always
the same. For this, we will use a cache system, which will store the result of a test in a file, and which will verify
that the result of the test is always the same. If the result of the test is different, then the test fails.

### Reverse tests

_this idea has been cancelled because it does not correspond to the purpose of pytest-lock and will be destined, perhaps, for another librairy._

~~This idea came from the fact that while watching the comments of a YouTube video (which I no longer remember) that it
was a shame not to be able to do "reverse" tests. The idea is that once we have done our unit tests, if they work, we
can test with "random" or "unexpected" variables, if the test fails it means everything is fine. The idea here is to
take this up by offering “reverse” tests based on the lock tests.~~

## Architecture

The plugin has his own cache system to store the result of the tests. Modules, classes must be able to easily support
additions (such as configurations, unforeseen functionality) through the use of design patterns

## Tasks

### branch: *"feature/fixture-lock-clean"*

* **Status:** _Finish_
* **Note:** This branch requires that the branch "feature/fixture-lock-method" be finalized.

- [ ] Add `clean-all` method to clean all cache files, even those who don't have tests associated with fixture `lock`
- [ ] Add `clean-unused` method to clean all cache files who don't have tests associated with fixture `lock`

---

### branch: *"feature/fixture-lock-data"*

* **Status:** _Finish_
* **Note:** This branch requires that the branch "feature/fixture-lock-method" be finalized.

- [ ] Add support for `lock.lock` data library in different formats (json, pickle, etc.)
  - [ ] Add pypi option for install this feature
    - [ ] `pip install pytest-lock[pandas]`
    - [ ] `pip install pytest-lock[polars]`
    - [ ] `pip install pytest-lock[numpy]`
    
  - [ ] Add support for `pandas.DataFrame`
  - [ ] Add support for `pandas.Series`
  - [ ] Add support for `polars.DataFrame`
  - [ ] Add support for `polars.Series`
  - [ ] Add support for `numpy.ndarray`


## Examples to test

### Lock tests examples

```python
from pytest_lock import FixtureLock


def test_something(lock: FixtureLock):
    args = [1, 2, 3]
    lock.lock(sum, (args,))  # use the lock function to lock the result of the test
    ...
``` 

```python
from pytest_lock import FixtureLock


def test_something(lock: FixtureLock):
    args = [1, 2, 3]
    lock.change_parser('.json')
    lock.lock(sum, (args,))  # use the lock function to lock the result of the test
    ...
``` 

```python
from pytest_lock import FixtureLock


def test_something(lock: FixtureLock):
    args = [1, 2, 3]
    lock.lock(sum, (args,), extension='.json')  # use the lock function to lock the result of the test
    ...
``` 

### Running tests examples

```bash
pytest
```

```bash
pytest --lock
```

```bash
pytest --lock --simulate
```

```bash
pytest --lock --only-skip
```

```bash
pytest --lock --lock-date 13/12/2023
```

```bash
pytest --lock --clean
```
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

this idea has been cancelled because it does not correspond to the purpose of pytest-lock and will be destined, perhaps, for another librairy.

~~This idea came from the fact that while watching the comments of a YouTube video (which I no longer remember) that it
was a shame not to be able to do "reverse" tests. The idea is that once we have done our unit tests, if they work, we
can test with "random" or "unexpected" variables, if the test fails it means everything is fine. The idea here is to
take this up by offering “reverse” tests based on the lock tests.~~

## Architecture

The plugin has his own cache system to store the result of the tests. Modules, classes must be able to easily support
additions (such as configurations, unforeseen functionality) through the use of design patterns

## Tasks

---

### branch: *"feature/fixture-lock-pickle"*

* **Status:** _Finish_
* **Note:** This branch requires that the branch "feature/fixture-lock-method" be finalized.

- [X] Add `pickle` extension for `lock.lock` to support more types of data

---


### branch: *"feature/fixture-update-lock-target"*

* **Status:** _Start_
* **Note:** This branch requires that the branch "feature/fixture-lock-method" be finalized.

- [ ] Cli argument `--lock` target only test with `lock` fixture

---

### branch: *"feature/fixture-lock-clean"*

* **Status:** _Start_
* **Note:** This branch requires that the branch "feature/fixture-lock-method" be finalized.

- [ ] If test use `--lock` and `--clean` argument, then clean all unused cache files
- [ ] If test use `--lock` and `--clean` argument and `--only-skip` argument, then do anything, it's certainly a mistake (why clean only test with existing lock ?)
- [ ] If test use `--lock` and `--clean` argument and `--simulate` argument, list all unused cache files who will be removed without remove them.
- [ ] If test use `--lock` and `--clean` argument and `--lock-date` argument, thrown exception (can't lock a remove cache file)

---

### branch: *"feature/fixture-lock-clean-all"*

* **Status:** _Start_
* **Note:** This branch requires that the branch "feature/fixture-lock-method" be finalized.

- [ ] If test use `--lock` and `--clean-all` argument, then clean all cache files
- [ ] If test use `--lock` and `--clean-all` argument and `--only-skip` argument, then do anything, it's certainly a mistake (why clean only test with existing lock ?)
- [ ] If test use `--lock` and `--clean-all` argument and `--simulate` argument, throw exception (why simulate clean ? clean remove all cache files)
- [ ] If test use `--lock` and `--clean-all` argument and `--lock-date` argument, thrown exception (can't lock a remove cache file)

---

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
    lock.change_parser('.pickle')
    lock.lock(sum, (args,))  # use the lock function to lock the result of the test
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

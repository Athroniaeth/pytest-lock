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

This idea came from the fact that while watching the comments of a YouTube video (which I no longer remember) that it
was a shame not to be able to do "reverse" tests. The idea is that once we have done our unit tests, if they work, we
can test with "random" or "unexpected" variables, if the test fails it means everything is fine. The idea here is to
take this up by offering “reverse” tests based on the lock tests.

## Architecture

The plugin has his own cache system to store the result of the tests. Modules, classes must be able to easily support
additions (such as configurations, unforeseen functionality) through the use of design patterns

## Tasks

### branch: *"feature/lock-fixture"*

* **Status:** _Not started_
* **Note:** Branch containing the base of the pytest fixture 'lock', it must be able to easily integrate new functions, CLI arguments, etc…

- [X] Add fixtures `lock`

### branch: *"feature/fixtures-lock-method"*

* **Status:** _Finish_
* **Note:** This branch requires that the branch "feature/lock-fixture" be finalized.

- [X] Add fixtures method `lock.lock` to lock the result of a test to a cache file
    - [X] If test use `lock.lock` and result was not locked, exception is thrown
    - [X] If test use `lock.lock` result is in the cache file and is the same as the result of the test, test is valid
    - [X] If test use `lock.lock` result is in the cache file and is not the same as the result of the test, test is
      invalid (failed)
    - [X] If test use `lock.lock` and `--lock` in cli argument, then start test and lock the result in cache file (Any
      result with __str__ method and Exception are supported)
    - [X] If test use `lock.lock` and `--simulate` in cli argument, then simulate the result of the test, not write to the cache file.
    - [X] If test use `--simulate` argument and not `--lock` argument, then it's invalid, throw exception

### branch: *"feature/fixture-lock-date-support"*

* **Status:** _Finished_
* **Note:** This branch requires that the branch "feature/fixture-lock-method" be finalized.

- [X] Add support for `pytest --lock --lock-date 13/12/2023`, if test has `lock` fixture, then lock the result of the
  test to a cache file with the date of the lock, if date was expired, then the test is skipped

### branch: *"feature/fixture-reversed-method"*

* **Status:** _Not started_
* **Note:** This branch requires that the branch "feature/lock-fixture" be finalized.

- [ ] Add fixtures method `lock.reversal` to reverse test with random or unexpected variables
    - [ ] If test use `lock.reversed` and `--lock` argument, the argument is useless, skip.
    - [ ] If test has `lock.reversed` and `--reversed` argument
        - [ ] If the result was not locked the plugin will skip the test
        - [ ] If the result was locked the plugin will check the type of the arguments of lock, if the test have
          list[int] as argument, then the plugin will check if the test failed with list[str], str, int, float, etc...
          and if it's the case, the test is valid
    - [ ] Add arguments for `lock.reversed` to specify type to check, additionally, replace, or replace_joined
      Note :

## Examples to test

### Lock tests examples

```py 
from typing import List
from pytest_lock import FixtureLock


def test_something(lock: FixtureLock):
    lock.lock(sum, ([1, 2, 3],))  # use the lock function to lock the result of the test
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

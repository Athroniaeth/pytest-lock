# Changelog

## Version v1.0.0
* **Date:** _2024-02-03_
* **Version:** _>=3.8 and <=3.12_
* Note : this version break major versioning, because old acceptation test fail for this reason

### branch: *"feature/lock-fixture"*

* **Status:** _Finish_
* **Note:** Branch containing the base of the pytest fixture 'lock', it must be able to easily integrate new functions, CLI arguments, etc…

- [X] Modified `--lock` argument, now target only test with `lock` fixture
  - [X] The tests with the `lock` fixture had `skipped` status, now they have `passed` status
  - [X] The tests without the `lock` fixture had `passed` status, now they have `skipped` status

### branch: *"feature/fixture-lock-pickle"*

* **Status:** _Finish_
* **Note:** This branch requires that the branch "feature/fixture-lock-method" be finalized.

- [X] Add `pickle` extension for `lock.lock` to support more types of data
- [X] Now `pickle` is the default extension for `lock.lock` if no extension is specified

### branch: *"feature/fixture-lock-clean"*

* **Status:** _Start_
* **Note:** This branch requires that the branch "feature/fixture-lock-method" be finalized.

- [X] If test use `--lock` and `--clean` argument, then clean all unused cache files
- [X] If test use `--lock` and `--clean` argument and `--only-skip` argument, then do anything, it's certainly a mistake (why clean only test with existing lock ?)
- [X] If test use `--lock` and `--clean` argument and `--simulate` argument, list all unused cache files who will be removed without remove them.
- [X] If test use `--lock` and `--clean` argument and `--lock-date` argument, thrown exception (can't lock a remove cache file)


## Version v0.1.2 
* **Date:** _2024-01-27_
* **Version:** _>=3.8 and <=3.12_

### branch: *"feature/lock-fixture"*

* **Status:** _Finish_
* **Note:** Branch containing the base of the pytest fixture 'lock', it must be able to easily integrate new functions, CLI arguments, etc…

- [X] Add fixtures `lock`


### branch: *"feature/fixtures-lock-method"*

* **Status:** _Finish_
* **Note:** This branch requires that the branch "feature/lock-fixture" be finalized.

- [X] Add fixtures method `lock.lock` to lock the result of a test to a cache file

    - [X] If test use `lock.lock` and result was not locked, exception is thrown
    - [X] If test use `lock.lock` result is in the cache file and is the same as the result of the test, test is valid
    - [X] If test use `lock.lock` result is in the cache file and is not the same as the result of the test, test is invalid (failed)

    - [X] If test use `lock.lock` and `--lock` in cli argument, then start test and lock the result in cache file.
    - [X] If test use `lock.lock` and `--simulate` in cli argument, then simulate the result of the test, not write to the cache file.
    - [X] If test use `lock.lock` and `--only-skip` in cli argument, then don't update lock if the result was not locked.
    - [X] If test use `lock.lock` and `--lock-date` in cli argument, then lock the result of the test to a cache file with the date of the lock, if date was expired, then the test is failed

    - [X] If test use `--simulate` argument and not `--lock` argument, then it's invalid, throw exception
    - [X] If test use `--lock-date` argument and not `--lock` argument, then it's invalid, throw exception
    - [X] If test use `--only-skip` argument and not `--lock` argument, then it's invalid, throw exception

### branch: *"feature/fixture-lock-date-support"*

* **Status:** _Finish_
* **Note:** This branch requires that the branch "feature/fixture-lock-method" be finalized.

- [X] Add support for `pytest --lock --lock-date 13/12/2023`, if test has `lock` fixture, then lock the result of the
  test to a cache file with the date of the lock, if date was expired, then the test is skipped

---

## Version v0.1.0
* **Date:** _2024-01-xx_
* **Version:** _xxxxxx_

The package upload tests on Pypi were awkwardly carried out with version `v0.1.0` and `v0.1.1`, the package being defective, these were removed but Pypi refuses to change the package contents even after use, even if no download has been made. The first version is therefore `v0.1.2`.

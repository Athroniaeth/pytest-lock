# Changelog
## v0.1.0
- Add `lock` fixture
- Add `lock.lock` method
- Add cli argument `--lock` to pytest
- Add functionality, if a test have `lock` fixture, then compare the result of the test with the result in the cache file
- Add functionality, if a test have `lock` and `--lock` cli argument, then lock the result of the test to a cache file
- Add functionality, if a test have `lock` and `--simulate` cli argument, then simulate the result of the test, not write to the cache file
- Add functionality, if a test have `lock` and `--only-skip` cli argument, then don't update lock if the result was not locked
- Add functionality, if a test have `lock` and `--lock-date` cli argument, then lock the result of the test to a cache file with the date of the lock, if date was expired, then the test is failed
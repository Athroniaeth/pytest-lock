# v0.1.0
- Add cli argument `--lock` to pytest
- Add functionality, if a test have `lock` fixture, then compare the result of the test with the result in the cache file
- Add functionality, if a test have `lock` and `--lock` cli argument, then lock the result of the test to a cache file
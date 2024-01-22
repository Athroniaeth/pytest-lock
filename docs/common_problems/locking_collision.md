# Locking collision
## Problem
You may encounter this problem:

```python
from pytest_lock import FixtureLock


def test_lock_sum(lock: FixtureLock):
    lock.lock(sum, ([],))
    lock.lock(sum, ([1, 2, 3],))
```

```bash
pytest --lock
```

```bash
pytest
```

```{error}
Failed: No lock found, please run the lock of this test.
```

The problem is that to differentiate between successful tests that are not due to locking and those that are in the process of being locked, `lock.lock` returns a skip rather than a passed to indicate that this test is not a successful test, nor failed because it is no longer a failed test. The problem is that skiped as failed terminates the execution of the test function, so future uses of lock.lock are simply ignored.

## Solution
Use `pytest.mark.parametrize` to run the test for each argument, so you can have the test lock for all arguments. Your next use of pytest will no longer return this error

```python
from typing import List

import pytest
from pytest_lock import FixtureLock

list_args = [
    [],
    [1, 2, 3],
]


@pytest.mark.parametrize("args", list_args)
def test_lock_sum(lock: FixtureLock, args: List[int]):
    lock.lock(sum, (args,))
```
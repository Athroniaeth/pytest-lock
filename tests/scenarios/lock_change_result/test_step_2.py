from typing import List

from pytest_lock import FixtureLock


def custom_sum(list_numbers: List[int]):
    return sum(list_numbers) + 1


def test_sum(lock_test: FixtureLock):
    args = [1, 2, 3]
    lock_test.lock(custom_sum, (args,))

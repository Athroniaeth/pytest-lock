"""Test scenario representing a "classic" pytest_lock test which will be used in Pytester"""

from pytest_lock import FixtureLock


def test_sum(lock_test: FixtureLock):
    """ Scenario """
    args = (1, 2, 3)
    lock_test.lock(sum, (args,))

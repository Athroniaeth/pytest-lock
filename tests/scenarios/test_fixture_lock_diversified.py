"""Test scenario representing a "classic" pytest_lock test which will be used in Pytester"""
import pytest

from pytest_lock import FixtureLock


@pytest.mark.parametrize("args", [
    # passed
    (),
    [],
    (1, 2, 3),
    [1, 2, 3],

    # failed
    ("1", "2", "3"),
    ["1", "2", "3"],
    ("a", "b", "c"),
    ["a", "b", "c"],
])
def test_sum(lock_test: FixtureLock, args):
    """ Scenario """
    lock_test.lock(sum, (args,))

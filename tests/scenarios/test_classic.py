"""Test scenario representing a "classic" test which will be used in Pytester"""


def test_sum():
    assert sum((1, 2, 3)) == 6

import pytest
from _pytest.pytester import Pytester
from pytest_lock.models.cache.lock import Lock
from pytest_lock.models.cache.signature import SignatureLock


def test_lock_eq_error(pytester: Pytester) -> None:
    """ Test the lock __eq__ ValueError. """
    lock = Lock(
        result="",
        function="",
        arguments="",
        result_type="",
        function_type="",
        arguments_type="",
        signature=SignatureLock.from_function(lambda: None),
    )

    with pytest.raises(NotImplementedError):
        var = lock == 1

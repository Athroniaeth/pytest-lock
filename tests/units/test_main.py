"""Test file for the __main__ file, used as an entry point for the "python -m pytest-lock" command."""

import pytest

from pytest_lock.models.exceptions import LockException
from pytest_lock.__main__ import main


def test_main_call():
    """Test the main call. (This test is designed to avoid 0% coverage). """
    with pytest.raises(LockException):
        main()

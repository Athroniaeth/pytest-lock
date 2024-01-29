"""Test scenario representing a "classic" pytest_lock test which will be used in Pytester"""
from typing import List, Any

import pytest

from pytest_lock import FixtureLock
from pytest_lock.parser_file.builder import ParserFileBuilder

list_valid_extensions = ['.pickle']  # ParserFileBuilder().mapping.keys()


@pytest.mark.parametrize("extension", list_valid_extensions)
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
def test_sum(lock_test: FixtureLock, extension: str, args: List[Any]):
    """ Scenario """
    lock_test.change_parser(extension)
    lock_test.lock(sum, (args,))

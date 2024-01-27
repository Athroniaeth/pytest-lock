import warnings
from abc import ABC
from typing import Any, Callable, Tuple, override

from pytest_lock.fixtures.base import FixtureBase


class MixinReversed(FixtureBase, ABC):
    """Mixin for lock.reversed fixture."""

    @override
    def reversed(self, function: Callable, arguments: Tuple[Any, ...]) -> None:
        warnings.warn("This method is not implemented and will be added in a future version", DeprecationWarning)
        raise NotImplementedError("This method is not implemented and will be added in a future version")

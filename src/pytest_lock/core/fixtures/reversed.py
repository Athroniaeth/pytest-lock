import warnings
from typing import Any, Callable, Tuple

from pytest_lock.core.fixtures.base import FixtureBase


class MixinReversed(FixtureBase):
    def reversed(self, function: Callable, arguments: Tuple[Any, ...]) -> None:
        warnings.warn(
            "This method is not implemented and will be added in a future version",
            DeprecationWarning,
        )
        raise NotImplementedError("This method is not implemented and will be added in a future version")

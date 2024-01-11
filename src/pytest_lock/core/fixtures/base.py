from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Callable, Tuple

from pytest_lock.core.cache import CacheLock
from pytest_lock.core.config import LockConfig


@dataclass
class FixtureBase(ABC):
    """Base class (for add mixins) for fixtures that use the lock."""

    config: LockConfig
    cache_system: CacheLock

    @abstractmethod
    def lock(self, function: Callable, arguments: Tuple[Any, ...]) -> None:
        pass

    """@abstractmethod
    def reversed(self, function: Callable, arguments: Tuple[Any, ...]) -> None:
        pass"""

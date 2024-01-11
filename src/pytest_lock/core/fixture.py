from pytest_lock.core.cache import CacheLock
from pytest_lock.core.config import LockConfig
from pytest_lock.core.fixtures.lock import MixinLock


class FixtureLock(MixinLock):
    """
    Fixture for pytest-lock given when user call 'lock' in pytest fixture.

    Mixins:
        MixinLock: Lock a function with arguments in a cache file, if the result don't change, the test is passed
        MixinReversed: Reversed a function with reversed arguments, if throw an error, the test is passed

    Args:
        config (LockConfig): The config of pytest-lock fixture
        cache_system (CacheLock): The cache system of pytest-lock fixture
    """

    def __init__(self, config: LockConfig, cache_system: CacheLock):
        super().__init__(config, cache_system)
        # init MixinLock and MixinReversed
        # super(MixinLock, self).__init__(config, cache_system)
        # super(MixinReversed, self).__init__(config, cache_system)

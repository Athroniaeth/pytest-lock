import logging
from typing import Optional

from pytest_lock.core.config import LockConfig
from pytest_lock.core.parser_file.base import ParserFile
from pytest_lock.models.cache.lock import Lock


class CacheLock:
    def __init__(self, config: LockConfig, parser: ParserFile):
        self.parser = parser
        self.cache_path = config.cache_path

    def write_lock(self, lock: Lock) -> None:
        file_cache = self.parser.read_file(self.cache_path)

        for index, other_lock in enumerate(file_cache.functions):
            if other_lock == lock:
                logging.info(f"Lock found, modified result {other_lock.result} with {lock.result}")
                file_cache.functions[index] = lock
                break
        else:
            logging.info(f"No lock found, create a new lock with result '{lock.result}'")
            file_cache.functions.append(lock)

        # write file_cache in path
        self.parser.write_file(self.cache_path, file_cache)

    def read_lock(self, lock: Lock) -> Optional[Lock]:
        if not self.cache_path.exists():
            return None

        file_cache = self.parser.read_file(self.cache_path)

        for index, other_lock in enumerate(file_cache.functions):
            if other_lock == lock:
                return other_lock

        return None

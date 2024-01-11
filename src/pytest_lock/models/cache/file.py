from dataclasses import dataclass
from typing import List

from pytest_lock.models.cache.lock import Lock
from pytest_lock.models.cache.signature import SignatureLock


@dataclass
class FileCache:
    functions: List[Lock]

    @classmethod
    def from_json(cls, json: dict):
        # SignatureLock(**signature) for signature in json["signatures"]
        functions = [Lock(**function) for function in json["functions"]]

        for index, lock in enumerate(functions):
            lock.signature = SignatureLock(**json["functions"][index]["signature"])

        return cls(functions=functions)

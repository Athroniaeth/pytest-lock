import json
from pathlib import Path

from pytest_lock.models.cache.file import FileCache
from pytest_lock.parser_file.base import ParserFile

try:
    from typing import override
except ImportError:
    from typing_extensions import override


class ParserFileJson(ParserFile):
    """
    Parser for json file.

    Attributes:
        encoding: Encoding of file
    """

    def __init__(self, encoding: str = "utf-8"):
        super().__init__(encoding=encoding)

    @override
    def read_file(self, path: Path) -> FileCache:
        if not path.exists():
            return FileCache(functions=[])
        content = path.read_text(encoding=self.encoding)
        json_content = json.loads(content)
        return FileCache.from_json(json_content)

    @override
    def write_file(self, path: Path, file_cache: FileCache) -> None:
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()

        content = json.dumps(file_cache, indent=4, default=lambda o: o.__dict__)
        path.write_text(
            content,
            encoding=self.encoding,
        )

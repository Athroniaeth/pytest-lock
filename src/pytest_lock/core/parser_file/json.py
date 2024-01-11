import json
from pathlib import Path

from pytest_lock.core.parser_file.base import ParserFile
from pytest_lock.models.cache.file import FileCache


class ParserFileJson(ParserFile):
    def __init__(self, encoding: str = "utf-8"):
        super().__init__(encoding=encoding)

    def read_file(self, path: Path) -> FileCache:
        if not path.exists():
            return FileCache(functions=[])
        content = path.read_text(encoding=self.encoding)
        json_content = json.loads(content)
        return FileCache.from_json(json_content)

    def write_file(self, path: Path, file_cache: FileCache) -> None:
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()

        content = json.dumps(file_cache, indent=4, default=lambda o: o.__dict__)
        path.write_text(
            content,
            encoding=self.encoding,
        )

from typing import Dict

from pytest_lock.core.parser_file.base import ParserFile
from pytest_lock.core.parser_file.json import ParserFileJson


class ParserFileBuilder:
    mapping: Dict[str, ParserFile]

    def __init__(self):
        self.mapping = {
            ".json": ParserFileJson(),
        }

    def build(self, extension: str = ".json") -> ParserFile:
        parser_file = self.mapping.get(extension)

        if parser_file is None:
            raise Exception("No parser_file file found")

        return parser_file

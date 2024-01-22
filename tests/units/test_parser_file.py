from pytest_lock.parser_file.builder import ParserFileBuilder
import pytest

list_valid_extensions = ParserFileBuilder().mapping.keys()


@pytest.mark.parametrize("extension", list_valid_extensions)
def test_parser_file_builder(extension: str):
    """Test the parser file builder."""
    builder = ParserFileBuilder()
    builder.build(".json")


def test_parser_file_builder_err():
    """Test the parser file builder."""
    builder = ParserFileBuilder()

    with pytest.raises(ValueError):
        builder.build("__not_exist__")

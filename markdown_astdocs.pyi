import re
import typing

from markdown.blockprocessors import BlockProcessor
from markdown.core import Markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
from xml.etree.ElementTree import Element

SOURCE_RE: str
START_RE: str
END_RE: str

def percent_source(path: str, lineno: int = ..., lineno_end: int = ...) -> str: ...
def percent_start() -> str: ...
def percent_end() -> str: ...

class AstdocsSourcePreprocessor(Preprocessor):
    path: typing.Any
    def __init__(self, md: Markdown, path: str) -> None: ...
    def run(self, lines: typing.List[str]) -> typing.List[str]: ...

class AstdocsStartEndBlockProcessor(BlockProcessor):
    def __init__(self, parser) -> None: ...
    def test(self, parent: Element, block: str) -> re.Match: ...
    def run(self, parent: Element, blocks: typing.List[str]) -> None: ...

class AstdocsExtension(Extension):
    config: typing.Any
    def __init__(self, **kwargs) -> None: ...
    def extendMarkdown(self, md: Markdown): ...
from typing import Any, Mapping
from bs4 import BeautifulSoup
from ..interface import AbstractParser


class SoupParser(AbstractParser):
    """Parser class with beautiful soup 4"""
    def __init__(self, content):
        self.content = content
        self._parser = BeautifulSoup(content, 'html.parser')
    
    def select(self, query: str, limit: int = None, **kwargs: Mapping) -> Any:
        result = self._parser.select(query, limit=limit, **kwargs)
        return result

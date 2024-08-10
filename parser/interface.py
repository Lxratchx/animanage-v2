from abc import ABC, abstractmethod
from typing import Any, Mapping


class AbstractParser(ABC):
    def __init__(self, content):
        """initializer method

        Args:
            content (Any): the page content to be parsed
        """

    @abstractmethod
    def select(self, query: str, limit: int=None, **kwargs: Mapping) -> Any:
        """fetch in the html DOM the given query using CSS method

        Args:
            query (str): the query to search into DOM
            limit (int, optional): the limit of elements to return. Defaults to None.
            kwargs (Mapping): kwargs passed to the original parser function
        
        Ex.:
        >>> some_parser.select(query, limit, **kwargs)
        """

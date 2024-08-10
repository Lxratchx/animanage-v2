from abc import ABC, abstractmethod
from typing import Literal, Any
from .dispatcher import RequestDispatcher

class AbstractRequester(ABC):
    def __init__(self, url: str|list[str], content_type: Literal['text', 'bytes']='text') -> None:
        """initializer method

        Args:
            url (str|list[str]): the url or list of the urls to request and fetch de page content
            content_type (Literal[&#39;text&#39;, &#39;bytes&#39;], optional): the type of the content fetched on the page. Defaults to 'text'.

            content_type_methods (dict[str, str]): the method names to get the content with the respective type using getattr method
            content_type_method (str): the method value of the repective content_type key in content_type_methods
        """
        self._url = url
        self._content_type = content_type
        self._dispatcher = RequestDispatcher()

        self.content_type_methods = {
            'text': 'text',
            'bytes': 'content'
        }
        self.content_type_method = self.content_type_methods[self._content_type]

    def fetch(self) -> Any:
        self._register_handlers()
        return self._dispatch()
    
    def _register_handlers(self) -> None:
        """make the registers of the dispatcher handlers"""
        self._dispatcher.add_handler(str, self._get_content)
        self._dispatcher.add_handler(list, self._get_contents)
    
    def _dispatch(self) -> None:
        """call the dispatch method of the dispatcher"""
        return self._dispatcher.dispatch(self._url.__class__)
        
    @abstractmethod
    def _get_content(self) -> str|bytes:
        """return the page content

        Returns:
            str | bytes
        """
    
    @abstractmethod
    def _get_contents(self) -> list[str|bytes]:
        """return a list of page contents

        Returns:
            list[str | bytes]
        """

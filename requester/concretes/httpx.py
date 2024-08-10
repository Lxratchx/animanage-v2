"""concrete implementation of a requester using httpx"""
from typing import Literal

import httpx

from requester.interface import AbstractRequester


class HttpX(AbstractRequester):
    """use httpx to make requests and to get the page content"""
    def __init__(self, url: str, content_type: Literal['text'] | Literal['bytes'] = 'text', use_async=False) -> None:
        super().__init__(url, content_type)
        self.use_async = use_async
    
    def _register_handlers(self) -> None:
        if self.use_async:
            self._dispatcher.add_handler(str, self.__aget_content)
            self._dispatcher.add_handler(list, self.__aget_contents)
        else:
            super()._register_handlers()
    
    def _get_content(self) -> str | bytes:
        response = httpx.get(self._url)
        page_content = getattr(response, self.content_type_method)
        return page_content
    
    def _get_contents(self) -> str | bytes:
        contents = []
        for url in self._url:
            response = httpx.get(url)
            page_content = getattr(response, self.content_type_method)
            contents.append(page_content)

        return contents
    
    async def __aget_content(self) -> str|bytes:
        """works like get_content but in async mode"""
        async with httpx.AsyncClient() as client:
            response = await client.get(self._url)
            page_content = getattr(response, self.content_type_method)
        
        return page_content
    
    async def __aget_contents(self) -> str|bytes:
        """works like get_contents but in async mode"""
        async with httpx.AsyncClient() as client:
            contents = []
            for url in self._url:
                response = await client.get(url)
                page_content = getattr(response, self.content_type_method)
                contents.append(page_content)
        
        return contents

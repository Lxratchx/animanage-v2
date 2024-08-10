from typing import Any
from requester.interface import AbstractRequester
from ..constants import ANIMES_URL


class AnimeExtractor:
    def __init__(self, requester: AbstractRequester, npages=3) -> None:
        self.requester = requester
        self.npages = npages + 1
    
    def extract(self) -> list[Any]:
        results = []
        for p in range(1, self.npages):
            url = ANIMES_URL 
            if p > 1:
                url += f'page/{p}/'

            req = self.requester(url)
            page_content = req.fetch()
            results.append(page_content)
        return results

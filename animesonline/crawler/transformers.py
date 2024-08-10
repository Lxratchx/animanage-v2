from typing import Any
from parser.interface import AbstractParser
from ..schemas import AnimesSchema, AnimeSchema


class AnimeTransformer:
    def __init__(self, data: Any, parser: AbstractParser) -> None:
        self._data = data
        self._parser = parser
    
    def transform(self) -> AnimesSchema:
        """makes all the necessary transformations to the anime's data

        Returns:
            AnimesSchema: an pydantic.BaseModel subclass object
        """
        parsed = [self._parser(d) for d in self._data]
        animes = AnimesSchema(animes=[])
        for parser in parsed:
            names = [i.text for i in parser.select('div.data h3 a')]
            urls = [i.get('href') for i in parser.select('div.data h3 a')]
            for n, u in zip(names, urls):
                anime = AnimeSchema(name=n, url=u)
                animes.animes.append(anime)
        return animes

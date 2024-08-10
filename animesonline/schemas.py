from pydantic import BaseModel, HttpUrl


class AnimeSchema(BaseModel):
    name: str
    url: HttpUrl


class AnimesSchema(BaseModel):
    animes: list[AnimeSchema]

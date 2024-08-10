from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..models import Anime

class AnimeLoader:
    def __init__(self, engine) -> None:
        self.engine = engine

    def load(self, data: BaseModel) -> bool:
        """load data of the animes to database

        Args:
            data (BaseModel) anime data like instances of a pydantic.BaseModel object.
        """
        with Session(self.engine) as session:
            for anime in data:
                anime = Anime(**anime.model_dump())
                q = session.query(Anime).filter(
                    Anime.name == anime.name or Anime.url == anime.url
                )
                if q.exists():
                    continue
                session.add(anime)
            
            session.commit()

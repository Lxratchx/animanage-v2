import re
from sqlalchemy.orm import validates, DeclarativeBase
from sqlalchemy import Column, String, Integer


class Base(DeclarativeBase): ...


class Anime(Base):
    __tablename__ = 'animes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    url = Column(String(2083), nullable=True, unique=True)

    @validates('name')
    def validate_name(self, key, name):
        assert re.match(r'\w+', name) is not None, 'Nome de anime inválido.'
        return name

    @validates('url')
    def validate_url(self, key, url):
        url_regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// ou https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domínios
            r'localhost|' # localhost
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # endereços IPv4
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # endereços IPv6
            r'(?::\d+)?' # porta opcional
            r'(?:/?|[/?]\S+)$',
            re.IGNORECASE
        )
        assert re.match(url_regex, url) is not None, f'URL de anime inválida.'
        return url

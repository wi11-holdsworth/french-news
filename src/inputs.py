from typing import Callable
from dateutil import parser
from babel.dates import format_datetime
from enum import Enum


class Field(Enum):
    TITLE = ["title"], lambda x: f"🇫🇷 {x}"
    SUMMARY = ["summary"]
    LINK = (["link"], lambda x: f"[Lire l'article en entier](<{x}>)")
    PUBLISHED = (
        ["published"],
        lambda x: f"Publié le "
        + format_datetime(parser.parse(timestr=x), locale="fr_FR"),
    )
    MEDIA_THUMBNAIL = (
        ["media_thumbnail", "media_content"],
        lambda x: f"[La vignette]({x[0]['url']})",
    )

    def __init__(self, aliases: list[str], fmt: Callable = lambda x: x):
        self.aliases: list[str] = aliases
        self.fmt: Callable = fmt


SOURCES: dict[str, dict] = {
    "Le Monde": {
        "url": "https://www.lemonde.fr/rss/une.xml",
        "max_fetch": 3,
    },
    "France 24": {
        "url": "https://www.france24.com/fr/france/rss",
        "max_fetch": 3,
    },
}

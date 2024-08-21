from inputs import Field
from feedparser import parse


def fetch_entries(url: str) -> list[dict]:
    return parse(url)["entries"]


def fmt_entry(entry: dict) -> dict[Field, str]:
    out: dict[Field, str] = {}

    for field in list(Field):
        for alias in field.aliases:
            if alias in entry:
                out[field] = field.fmt(entry[alias])

    return out


def structure_entry(fmt: dict[Field, str]) -> str:
    return (
        f"## {fmt[Field.TITLE]}\n"
        + f"> {fmt[Field.SUMMARY]}\n\n"
        + f"📰 {fmt[Field.LINK]}\n"
        + f"🖼 {fmt[Field.MEDIA_THUMBNAIL]}\n\n"
        + f"-# {fmt[Field.PUBLISHED]}\n"
    )


def entry_to_msg(entry: dict) -> str:
    return structure_entry(fmt_entry(entry))

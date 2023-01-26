from invoke import task
from enum import Enum
from pathlib import Path


class SpidersTypes(Enum):
    """Types of spiders."""
    authors="authors"
    quotes="quotes"
    tag_quotes="tag-quotes"


DEFAULT_PARSE_PATH = "data/{file_name}.json"


@task
def parse(context, spider: SpidersTypes):
    """Parse spider."""
    print("Parsing...")
    path = Path(DEFAULT_PARSE_PATH.format(file_name=spider))
    context.run(f"scrapy crawl {spider} -O {path}")
    print("Parsing is finished!")

from typing import Self
from pydantic import BaseModel

from var import MyFiles
from models import Category, Entry, Site

class Data(BaseModel):

    categories: list[Category]
    entries: list[Entry]
    site: Site

    @staticmethod
    def parse(cfile: str, efile: str, tfile: str) -> Self:
        categories = sorted(Category.parse(cfile), key=lambda x: x.name)
        entries = sorted(Entry.parse(efile, categories), key=lambda x: x.difficulty)

        return Data(
            categories = categories,
            entries = entries,
            site = Site.parse(tfile)
        )

    def get_category(self, id: str) -> Category | None:
        for c in self.categories:
            if c.id == id:
                return c
        return None


class DataLoader:

    data: Data

    def __init__(self, cfile: str = MyFiles.Data.CATEGORIES, efile: str = MyFiles.Data.ENTRIES, tfile: str = MyFiles.Data.SITE):
        self.data = Data.parse(cfile, efile, tfile)

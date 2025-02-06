from typing import Self
from pydantic import BaseModel

from var import MyVars
from models import Category, Entry, Site

class Data(BaseModel):
        
    categories: list[Category]
    entries: list[Entry]
    site: Site
    
    @staticmethod
    def parse(cfile: str, efile: str, tfile: str) -> Self:
        categories = Category.parse(cfile)
        return Data(
            categories = categories,
            entries = Entry.parse(efile, categories),
            site = Site.parse(tfile)
        )
    
    def get_category(self, id: str) -> Category | None:
        for c in self.categories:
            if c.id == id:
                return c
        return None
        

class DataLoader:
    
    data: Data
    
    def __init__(self, cfile: str = MyVars.Data.CATEGORIES, efile: str = MyVars.Data.ENTRIES, tfile: str = MyVars.Data.SITE):
        self.data = Data.parse(cfile, efile, tfile)
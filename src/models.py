from pydantic import BaseModel
from typing import Self

from util import MyUtil


class Category(BaseModel):
    id: str
    type: str
    name: str
    
    @staticmethod
    def parse(cfile: str) -> list[Self]:
        categories = []
        cf_conts = MyUtil.File.read_csv(cfile)
        for c in cf_conts:
            categories.append(
                Category(
                    id=c[0],
                    type=c[1],
                    name=c[2]
                )
            )
        return categories
    
    @staticmethod
    def search(id: str, categories: list[Self]) -> Self | None:
        for c in categories:
            if id == c.id:
                return c
        return None
    
class Entry(BaseModel):
    id: str
    category_id: str
    question: str
    answer: str
    difficulty: int
    category: Category | None = None
    
    @staticmethod
    def parse(efile: str, categories: list[Category]) -> list[Self]:
        entries = []
        f_conts = MyUtil.File.read_csv(efile)
        for r in f_conts:
            entries.append(
                Entry(
                    id=r[0],
                    category_id=r[1],
                    question=r[2],
                    answer=r[3],
                    difficulty=int(r[4]),
                    category=Category.search(id=r[1], categories=categories)
                )
            )
        return entries
    
class Site(BaseModel):
    class Metadata(BaseModel):
        name: str
        version: str
        icon: str = ""
    
    class Content(BaseModel):
        type: str
        contents: str = ""
        
    metadata: Metadata
    content: list[Content]
    
    @staticmethod
    def parse(tfile: str) -> Self:
        toml = MyUtil.File.read_toml(tfile)
        metadata = Site.Metadata(**toml["metadata"])
        content = []
        for ctnt in toml["content"]:
            content.append(
                Site.Content(**ctnt)
            )
        return Site(metadata=metadata,content=content)
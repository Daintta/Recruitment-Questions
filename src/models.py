from pydantic import BaseModel
from typing import Self

from util import MyUtil


class Category(BaseModel):
    id: str
    type: str
    name: str
    
    @staticmethod
    def parse(cfile: str) -> list[Self]:
        return [
            Category(
                id=c[0],
                type=c[1],
                name=c[2]
            )
            for c in MyUtil.File.read_csv(cfile)
        ]
    
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
        return [
            Entry(
                id=r[0],
                category_id=r[1],
                question=r[2],
                answer=r[3],
                difficulty=int(r[4]),
                category=Category.search(id=r[1], categories=categories)
            )
            for r in MyUtil.File.read_csv(efile)
        ]
    
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
        content = [Site.Content(**ctnt) for ctnt in toml["content"]]
        return Site(metadata=metadata,content=content)
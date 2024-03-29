

from typing import List
from pydantic import BaseModel


class NamedUrls(BaseModel):
    name: str
    url: List[str]

class PositionInfo(BaseModel):
    company: str
    position: str
    name: str
    blog_articles: List[str]
    youtube_interviews: List[NamedUrls]


class PositionInfoList(BaseModel):
    positions: List[PositionInfo]
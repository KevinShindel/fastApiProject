from pydantic import BaseModel
from pydantic.class_validators import Optional


class Point(BaseModel):
    id: Optional[int]
    coords: list
    title: str
    text: str

    class Config:
        orm_mode = True


class PointCreate(Point):
    pass

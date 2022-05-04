from sqlalchemy import Column, Integer, String, PickleType
from sqlalchemy.ext.mutable import MutableList

from sql_app.database import Base


class Point(Base):
    __tablename__ = 'map_points'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    coords = Column(MutableList.as_mutable(PickleType), default=[])
    title = Column(String)
    text = Column(String)

    def __str__(self):
        return self.__module__.__class__.__name__

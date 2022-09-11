#!/usr/bin/python3
"""
defines a City class
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class City(Base):
    """
    Defines a city model that inherits from Base
    """

    __tablename__ = "cities"
    id = Column(Integer, nullable=False, unique=True, autoincrement=True)
    name = Coumn(String(128), nulable=False)
    state_id  Column(Integer, ForeignKey('states.id'), nullable=False)

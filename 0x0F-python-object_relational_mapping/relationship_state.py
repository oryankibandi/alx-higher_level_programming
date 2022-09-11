#!/usr/bin/python3
"""
State Model
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    Object represtation of states
    """

    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

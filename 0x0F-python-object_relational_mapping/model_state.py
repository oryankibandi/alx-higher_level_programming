#!/usr/bin/python3
"""
SQLAlchemy implementation
"""

from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Object representation of the states table
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=true, nullable=False, primary_key=True,
            unique=True, autoincrement=True)
    name = Column(String(128), nulable=False)

#!/usr/bin/env python3
"""
User model definition
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy model for the users table
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)


# Code to create the table in the database
if __name__ == "__main__":
    engine = create_engine('sqlite:///users.db')
    Base.metadata.create_all(engine)

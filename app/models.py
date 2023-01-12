# логика связанная с подключением к базе данных и модели которые сделаны с помощью sqlalchemy
from datetime import datetime
from enum import Enum

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.exc.declarative import declarative_base


from app.config import DATABASE_URL

Base = declarative_base()


class PostStatus(Enum):
    PLANED = "planed"
    ACTIVE = "active"
    CLOSED = "closed"


def connect_db():
    engine = create_engine(DATABASE_URL, connect_args={})
    session = Session(bind=engine.connect())
    return session


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    nickname = Column(String)
    created_at = Column(String, default=datetime.utcnow())


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    title = Column(String)
    topic = Column(String)
    status = Column(String)
    created_at = Column(String, default=datetime.utcnow())



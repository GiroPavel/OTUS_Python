from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("postgresql://pavel.giro:password@localhost:5432/postgres")
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

class JsonPlaceholderUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    email = Column(String, unique=True)


class JsonPlaceholderPost(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    body = Column(String, unique=True)

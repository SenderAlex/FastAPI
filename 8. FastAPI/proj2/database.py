from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_URL = 'sqlite:///./db1.db'  # параметры подключения БД
engine = create_engine(DB_URL)  # движок нашей БД (создается engine, подрубается наша БД по указанному url)
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()  # создаем нашу БД, объявляем нашу БД


def get_session():  # функция, которая, позволяет получить нашу БД
    db = session()
    try:
        yield db
    finally:
        db.close()
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, func
from models import UserModel, Base
import time
import datetime

engine = create_engine('postgresql://app:1234@127.0.0.1:5431/app')
Session = sessionmaker(bind=engine)


@pytest.fixture(scope='session', autouse=True)  #запускается в начале сессии
def prepare_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


@pytest.fixture()                   # тестовый клиент
def create_article():
    with Session() as session:
        new_article = UserModel(headline=f'{time.time()}title', owner='Mary', description='bla')
        session.add(new_article)
        session.commit()
        return {
            'art_id': new_article.art_id,
            'headline': new_article.headline,
            'description': new_article.description,
            'owner': new_article.owner
        }











# import datetime
# import time
# from dataclasses import dataclass
#
# import pytest
# import requests
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# from tests.api import login
# from config import PG_USER, PG_PASSWORD, PG_HOST, PG_PORT, PG_DB
# from models import Base, User
# from auth import hash_password
# from tests.config import API_URL
#
# engine = create_engine(f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}")
# Session = sessionmaker(bind=engine)
#
#
# @dataclass
# class UserData:
#     id: int
#     name: str
#     password: str
#     creation_time: datetime.datetime
#
#
# @pytest.fixture(scope="session", autouse=True)
# def init_database():
#
#     Base.metadata.drop_all(bind=engine)
#     Base.metadata.create_all(bind=engine)
#     yield
#     engine.dispose()
#
#
# def create_user(name: str, password: str):
#     with Session() as session:
#         password = hash_password(password)
#         new_user = User(name=name, password=password)
#         session.add(new_user)
#         session.commit()
#         return UserData(id=new_user.id, name=name, password=password, creation_time=new_user.creation_time)
#
#
# @pytest.fixture(scope="session", autouse=True)
# def root_user():
#     return create_user("root", "toor")
#
#
# @pytest.fixture(scope="session", autouse=True)
# def root_user_token():
#     return login("root", "toor")["token"]
#
#
# @pytest.fixture()
# def new_user():
#     name = f"new_user_{time.time()}"
#     return create_user(name, "1234")

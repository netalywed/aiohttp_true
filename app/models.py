from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, func

engine = create_async_engine('postgresql+asyncpg://app:1234@127.0.0.1:5431/app')
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


class UserModel(Base):

    __tablename__ = "app_articles"

    art_id = Column(Integer, primary_key=True, autoincrement=True)
    headline = Column(String, unique=True, nullable=False, index=True)
    description = Column(String)
    creation_date = Column(DateTime, server_default=func.now())
    owner = Column(String, nullable=False)











# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
#
#
# Base = declarative_base()
#
#
# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(64), unique=True, nullable=False)
#     password = Column(String(60), nullable=False)
#     creation_time = Column(DateTime, server_default=func.now())
#
#
# class Token(Base):
#     __tablename__ = "tokens"
#
#     id = Column(UUID, server_default=func.uuid_generate_v4(), primary_key=True)
#     user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
#     user = relationship("User", lazy="joined")
#     creation_time = Column(DateTime, server_default=func.now())

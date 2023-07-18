from sqlalchemy import Column, Integer, String

from .database import Base


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    phone_work = Column(String, index=True)
    first_name = Column(String)
    last_name = Column(String)

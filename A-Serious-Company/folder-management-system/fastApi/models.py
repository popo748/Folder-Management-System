from fastApi.database import Base
from sqlalchemy import Column, Integer, String

class Folders(Base):
    __tablename__ = "folders"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    
from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Civilization(Base):
    __tablename__ = "civilizations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    name_civilization = Column(String, nullable=False)
    linguistic_system = Column(String, nullable=False)  # Fixed typo: languistic -> linguistic
    new_words = Column(String, nullable=False)
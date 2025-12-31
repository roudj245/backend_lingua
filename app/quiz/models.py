from sqlalchemy import Column, Integer, String, Float, UniqueConstraint
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    score = Column(Integer, default=0)
    
    # Ensure unique combination of name and lastname
    __table_args__ = (
        UniqueConstraint('name', 'lastname', name='unique_name_lastname'),
    )



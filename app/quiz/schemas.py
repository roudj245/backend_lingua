from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    lastname: str
    score: int


class UserUpdate(BaseModel):
    score: int


class UserResponse(BaseModel):
    id: int
    name: str
    lastname: str
    score: int

    class Config:
        from_attributes = True
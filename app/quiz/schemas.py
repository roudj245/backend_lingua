from pydantic import BaseModel


class UserCreate(BaseModel):
    score: int
    name: str


class UserResponse(BaseModel):
    id: int
    name: str
    score: int

    class Config:
        from_attributes = True

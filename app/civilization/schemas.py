from pydantic import BaseModel, Field


class CivilizationCreate(BaseModel):
    name: str
    civilization: str
    linguistic_system: str
    new_words: str

    class Config:
        populate_by_name = True


class CivilizationResponse(BaseModel):
    id: int
    name: str
    name_civilization: str
    linguistic_system: str
    new_words: str

    class Config:
        from_attributes = True
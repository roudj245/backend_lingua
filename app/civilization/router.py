from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.civilization.schemas import CivilizationCreate, CivilizationResponse
from app.civilization.service import (
    create_civilization,
    get_civilization,
    get_all_civilizations,
)

router = APIRouter(prefix="/civilizations", tags=["civilizations"])


@router.post("/", response_model=CivilizationResponse)
def create_new_civilization(civ: CivilizationCreate, db: Session = Depends(get_db)):
    return create_civilization(db, civ)


@router.get("/{civ_id}", response_model=CivilizationResponse)
def get_civ(civ_id: int, db: Session = Depends(get_db)):
    result = get_civilization(db, civ_id)
    if not result:
        raise HTTPException(status_code=404, detail="Civilization not found")
    return result


@router.get("/", response_model=list[CivilizationResponse])
def get_all_civs(db: Session = Depends(get_db)):
    return get_all_civilizations(db)
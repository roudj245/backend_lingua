
from sqlalchemy.orm import Session
from app.civilization.models import Civilization
from app.civilization.schemas import CivilizationCreate, CivilizationResponse


def create_civilization(db: Session, civ: CivilizationCreate) -> CivilizationResponse:
    db_civ = Civilization(
        name=civ.name,
        name_civilization=civ.civilization,
        linguistic_system=civ.linguistic_system,
        new_words=civ.new_words
    )
    db.add(db_civ)
    db.commit()
    db.refresh(db_civ)
    return db_civ


def get_civilization(db: Session, civ_id: int) -> CivilizationResponse:
    civ = db.query(Civilization).filter(Civilization.id == civ_id).first()
    if not civ:
        return None
    return civ


def get_all_civilizations(db: Session) -> list[CivilizationResponse]:
    civs = db.query(Civilization).all()
    return civs

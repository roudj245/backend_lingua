from sqlalchemy.orm import Session
from app.quiz.models import User
from app.quiz.schemas import UserCreate, UserResponse


def create_user(db: Session, user: UserCreate) -> UserResponse:
    db_user = User(name=user.name, score=user.score)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_score_user(db: Session, user_id: int) -> UserResponse:
    user = db.query(User).filter(User.id == user_id).first()
    return user


def get_user_score_all(db:Session)->list[UserResponse]:
    users = db.query(User).order_by(User.score.desc()).all()
    return users


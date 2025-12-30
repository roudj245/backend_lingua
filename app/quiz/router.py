from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.quiz.schemas import UserCreate, UserResponse
from app.quiz.service import create_user, get_score_user, get_user_score_all

router = APIRouter(prefix="/quiz", tags=["quiz"])


@router.post("/users", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user_score(user_id: int, db: Session = Depends(get_db)):
    return get_score_user(db, user_id)


@router.get("/users", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return get_user_score_all(db)

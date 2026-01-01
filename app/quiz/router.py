from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.quiz.schemas import UserCreate, UserResponse, UserUpdate
from app.quiz.service import create_or_update_user, get_score_user, get_user_score_all, update_user_score, delete_all_users

router = APIRouter(prefix="/quiz", tags=["quiz"])


@router.post("/users", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_or_update_user(db, user)


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user_score(user_id: int, db: Session = Depends(get_db)):
    return get_score_user(db, user_id)


@router.get("/users", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return get_user_score_all(db)


@router.put("/users/{name}/{lastname}", response_model=UserResponse)
def update_user(name: str, lastname: str, user_update: UserUpdate, db: Session = Depends(get_db)):
    user = update_user_score(db, name, lastname, user_update)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users", status_code=204)
def delete_users(db: Session = Depends(get_db)):
    delete_all_users(db)






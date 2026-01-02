from sqlalchemy.orm import Session
from app.quiz.models import User
from app.quiz.schemas import UserCreate, UserResponse, UserUpdate
from fastapi import HTTPException


def create_or_update_user(db: Session, user: UserCreate) -> UserResponse:
    # Check if user with same name and lastname exists
    existing_user = db.query(User).filter(
        User.name == user.name,
        User.lastname == user.lastname
    ).first()
    
    if existing_user:
        # Update existing user's score only if new score is higher
        if user.score > existing_user.score:
            existing_user.score = user.score
            db.commit()
            db.refresh(existing_user)
        return existing_user
    else:
        # Create new user
        db_user = User(name=user.name, lastname=user.lastname, score=user.score)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


def get_score_user(db: Session, user_id: int) -> UserResponse:
    user = db.query(User).filter(User.id == user_id).first()
    return user


def get_user_score_all(db: Session) -> list[UserResponse]:
    users = db.query(User).order_by(User.score.desc()).all()
    return users


def update_user_score(db: Session, name: str, lastname: str, user_update: UserUpdate) -> UserResponse:
    user = db.query(User).filter(
        User.name == name,
        User.lastname == lastname
    ).first()
    
    if user:
        # Update score only if new score is higher
        if user_update.score > user.score:
            user.score = user_update.score
            db.commit()
            db.refresh(user)
    
    return user


def delete_all_users(db: Session) -> str:
    db.query(User).delete()
    db.commit()
    return "All users deleted successfully"



def delete_user(db: Session, user_id: int) -> str:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return "User deleted successfully"






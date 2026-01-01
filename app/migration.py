from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/migrate-add-lastname")
def migrate_add_lastname(db: Session = Depends(get_db)):
    """
    Migration endpoint to add lastname column to existing users table.
    Run this ONCE after deploying the new code.
    """
    try:
        # Check if column already exists
        check_query = text("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name='users' AND column_name='lastname';
        """)
        result = db.execute(check_query).fetchone()
        
        if result:
            return {"message": "Column 'lastname' already exists. Migration not needed."}
        
        # Add lastname column
        db.execute(text("ALTER TABLE users ADD COLUMN lastname VARCHAR;"))
        
        # Set default value for existing users
        db.execute(text("UPDATE users SET lastname = 'Unknown' WHERE lastname IS NULL;"))
        
        # Make it NOT NULL
        db.execute(text("ALTER TABLE users ALTER COLUMN lastname SET NOT NULL;"))
        
        # Add unique constraint
        db.execute(text("ALTER TABLE users ADD CONSTRAINT unique_name_lastname UNIQUE (name, lastname);"))
        
        db.commit()
        
        return {
            "message": "Migration successful! Column 'lastname' added to users table.",
            "status": "success"
        }
    except Exception as e:
        db.rollback()
        return {
            "message": f"Migration failed: {str(e)}",
            "status": "error"
        }


@router.delete("/clear-all-users")
def clear_all_users(db: Session = Depends(get_db)):
    """
    DELETE ALL USERS FROM DATABASE
    WARNING: This cannot be undone!
    """
    try:
        from app.quiz.models import User
        
        # Count users before deletion
        count = db.query(User).count()
        
        # Delete all users
        db.query(User).delete()
        db.commit()
        
        return {
            "message": f"Successfully deleted {count} users from database.",
            "deleted_count": count,
            "status": "success"
        }
    except Exception as e:
        db.rollback()
        return {
            "message": f"Failed to delete users: {str(e)}",
            "status": "error"
        }
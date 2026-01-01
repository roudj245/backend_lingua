from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")

# PostgreSQL connection requires different handling than SQLite
if "sqlite" in DATABASE_URL:
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
else:
    # For PostgreSQL (Render provides DATABASE_URL in postgres:// format)
    # Need to convert to postgresql:// for SQLAlchemy 1.4+
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,  # Verify connections before using them
        pool_size=40,  # Base connection pool - always ready
        max_overflow=50,  # Additional connections during peaks (total: 90)
        pool_recycle=3600,  # Recycle connections after 1 hour
        pool_timeout=20,  # Wait max 20 seconds for available connection
        echo_pool=False,  # Disable pool logging for performance
        pool_use_lifo=True  # Use most recently returned connections first (faster)
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
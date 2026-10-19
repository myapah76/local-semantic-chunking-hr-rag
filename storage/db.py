import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from storage.models import Base

# Database connection URL
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("POSTGRES_DB", "hr_tech")

DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = None
SessionLocal = None

def get_engine():
    global engine, SessionLocal
    if engine is None:
        engine = create_engine(DATABASE_URL, pool_pre_ping=True, echo=False)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return engine

def init_db():
    """Create all tables if they do not exist."""
    eng = get_engine()
    Base.metadata.create_all(bind=eng)

def get_db():
    """Dependency or generator yielding a database session."""
    get_engine()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

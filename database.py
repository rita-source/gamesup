from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./boardgames.db"  # ou une autre base (PostgreSQL, MySQL, etc.)

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Fonction pour obtenir une session DB via dependency injection dans FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from crud.games import get_games

router = APIRouter(prefix="/games", tags=["games"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_games(db: Session = Depends(get_db)):
    return get_games(db)

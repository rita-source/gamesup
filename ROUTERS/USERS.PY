from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from crud.users import get_user

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)

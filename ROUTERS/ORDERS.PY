from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal  
from crud.orders import get_orders

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/orders")
def read_orders(db: Session = Depends(get_db)):
    # Appel de la fonction get_orders avec l'argument db
    return get_orders(db=db)

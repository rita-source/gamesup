from sqlalchemy.orm import Session
from models import Order

def get_orders(db: Session):
    
    return db.query(Order).all()  
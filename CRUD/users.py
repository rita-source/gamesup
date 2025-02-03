

from sqlalchemy.orm import Session
from models import User  

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate


def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, password=user.password)
    db.add(db_user) 
    db.commit()  
    db.refresh(db_user)  
    return db_user




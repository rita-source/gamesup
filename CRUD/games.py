from sqlalchemy.orm import Session
from models import Game

def get_games(db: Session):
    return db.query(Game).all()

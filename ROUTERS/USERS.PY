from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from crud.users import get_user
from schemas import UserCreate

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


@router.post("/users", response_model=UserCreate)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
  
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    return create_user(db=db, user=user)

@router.post("/users/")
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
   
    return create_user(db=db, user=user)

@router.post("/users", response_model=UserCreate)
async def create_user_endpoint(user: UserCreate):
    return await create_user(user)
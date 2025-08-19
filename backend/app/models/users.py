from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models
from ..database import get_db

router = APIRouter()

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.user.User).all()

@router.post("/")
def create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    user = models.user.User(
        username=username,
        email=email,
        hashed_password=password  # 🚨 En el futuro usar bcrypt
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
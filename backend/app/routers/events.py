from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models
from ..database import get_db

router = APIRouter()

@router.get("/")
def get_events(db: Session = Depends(get_db)):
    return db.query(models.event.Event).all()

@router.post("/")
def create_event(source_ip: str, destination_ip: str, protocol: str, description: str, db: Session = Depends(get_db)):
    event = models.event.Event(
        source_ip=source_ip,
        destination_ip=destination_ip,
        protocol=protocol,
        description=description
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return event
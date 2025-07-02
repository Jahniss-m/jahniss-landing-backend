from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from app.schemas import MessageCreate
from app.models import Message
from app.database import get_db
from app.utils import send_email

router = APIRouter()

@router.post("/contact")
def create_message(
    name: str = Form(...),
    email: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db)
):
    # Creamos el objeto MessageCreate para validación y envío
    msg = MessageCreate(name=name, email=email, content=content)
    
    message = Message(name=msg.name, email=msg.email, content=msg.content)
    db.add(message)
    db.commit()
    db.refresh(message)
    
    send_email(msg)
    return {"message": "Mensaje recibido"}

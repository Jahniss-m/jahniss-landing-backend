from pydantic import BaseModel, EmailStr

class MessageCreate(BaseModel):
    name: str
    email: EmailStr
    content: str
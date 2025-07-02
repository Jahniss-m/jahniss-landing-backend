from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as contact_router
from app.database import Base, engine
from app.models import Message  # Import necesario para registrar el modelo

app = FastAPI()

# Crear las tablas en la base de datos (solo la primera vez)
Base.metadata.create_all(bind=engine)

origins = ["*"]  # Cambia si quieres restringir orígenes

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contact_router)

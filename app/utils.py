import smtplib
from email.mime.text import MIMEText
from app.schemas import MessageCreate
import os

def send_email(msg: MessageCreate):
    sender = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    recipient = "soledadsatide1979@gmail.com"

    body = f"Nombre: {msg.name}\nCorreo: {msg.email}\nMensaje: {msg.content}"
    msg = MIMEText(body)
    msg["Subject"] = "Nuevo mensaje desde tu landing page"
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())
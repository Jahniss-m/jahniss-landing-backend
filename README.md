# Backend para la Landing Page de Jahniss

## Funcionalidad

- Endpoint `/contact` para recibir mensajes del formulario.
- Guarda los mensajes en una base de datos SQLite.
- Envía notificaciones por correo al recibir un mensaje.

## Cómo usar

1. Crea un archivo `.env` a partir de `.env.example` con tu correo y contraseña de aplicación.
2. Ejecuta `uvicorn app.main:app --reload` para desarrollo local.
3. Sube a Render siguiendo las instrucciones del README.
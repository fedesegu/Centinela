from fastapi import FastAPI
from .database import engine, Base
from .routers import users, events

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CyberGuard API",
    description="API para monitorear y analizar tráfico de red",
    version="0.1.0"
)

# Routers
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(events.router, prefix="/api/events", tags=["Events"])

@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "CyberGuard API funcionando 🚀"}
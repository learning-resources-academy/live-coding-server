from pydantic import BaseModel
from datetime import datetime

class Log(BaseModel):
    timestamp: datetime        # Fecha y hora en ISO
    service_name: str           # Nombre del servicio
    severity: str               # Nivel de severidad
    message: str                # Mensaje descriptivo

from fastapi import APIRouter, Header, Query
from fastapi.responses import JSONResponse
from models.models_logs import Log_schema
from db.db_logs import db_logs
from datetime import datetime

router = APIRouter(prefix="/logging", tags=["Logging"])

TOKEN_VALIDO = 'token_super_secreto_123'

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from db.db_logs import db_logs

router = APIRouter(prefix="/logging", tags=["Logging"])

@router.get("/logs")
def get_logs(
    severity: str = Query(None, description="Filtrar por nivel: INFO, WARNING, ERROR, DEBUG"),
    service_name: str = Query(None, description="Filtrar por nombre del servicio")
):
    """
    Retorna todos los logs o filtrados por nivel (severity) y/o servicio.
    """

    resultados = db_logs.copy()

    # 1️⃣ Filtrar por severity
    if severity:
        resultados = [
            log for log in resultados
            if log["severity"].upper() == severity.upper()
        ]

    # 2️⃣ Filtrar por service_name
    if service_name:
        resultados = [
            log for log in resultados
            if log["service_name"].lower() == service_name.lower()
        ]

    return JSONResponse(
        status_code=200,
        content={
            "total": len(resultados),
            "logs": resultados
        }
    )


@router.post("/logs")
async def add_log(log: Log_schema, Authorization: str = Header(None)):
    # 1. No hay token
    if not Authorization:
        return JSONResponse(
            status_code=401,
            content={"error": "No hay token, si no me das el token yo no te doy nada eh.."}
        )

    # 2. Token inválido
    if Authorization != TOKEN_VALIDO:
        return JSONResponse(
            status_code=401,
            content={"error": "Token incorrecto, quien sos bro?"}
        )

    # 3. Guardar directamente el log (ya validado por Pydantic)
    db_logs.append(log.dict())

    return JSONResponse(
        status_code=201,
        content={
            "message": "Log guardado",
            "total_logs": len(db_logs)
        }
    )
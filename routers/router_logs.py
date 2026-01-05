from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from models.models_logs import Log_schema
from db.db_logs import db_logs

router = APIRouter(prefix="/logging", tags=["Logging"])

TOKEN_VALIDO = 'token_super_secreto_123'

@router.get("/logs")
def get_logs():
    return db_logs

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
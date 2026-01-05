from fastapi import APIRouter
from models.models_logs import Log
from services.router_logs import create_log
from db.db_logs import db_logs

router = APIRouter(prefix="/logging", tags=["Logging"])

@router.get("/logs")
def get_logs():
    return db_logs

@router.post("/logs")
def add_log(log: Log):
    """Recibe un body con timestamp, service_name, severity y message"""
    return create_log(log)

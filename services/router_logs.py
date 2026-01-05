from fastapi import APIRouter

router = APIRouter(
    prefix="/logging",
    tags=["Logging"]
)

@router.get("/logs")
def get_logs():
    return {"challenge": "logging", "action": "listar logs"}

@router.post("/logs")
def create_log():
    return {"challenge": "logging", "action": "crear log"}

@router.get("/logs/{level}")
def get_logs_by_level(level: str):
    return {"level": level}
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Penguin Academy API",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def home():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

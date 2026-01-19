# apps/api/api/main.py
from fastapi import FastAPI

app = FastAPI(title="GharGPT API")


@app.get("/")
def root():
    return {"status": "ok"}

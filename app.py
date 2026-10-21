
from fastapi import FastAPI

app = FastAPI(
    title="PackCheck AI",
    description="ML-powered packaged commodity label analysis",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "project": "PackCheck AI",
        "status": "running",
        "message": "Welcome to PackCheck AI ML Edition!"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

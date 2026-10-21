
from fastapi import FastAPI
from pydantic import BaseModel
from ml_model import analyze_label

app = FastAPI(
    title="PackCheck AI-ML",
    description="Packaged commodity label analysis API",
    version="1.0.0",
)


class LabelData(BaseModel):
    product_name: str = ""
    manufacturer: str = ""
    net_quantity: str = ""
    mrp: str = ""
    consumer_care: str = ""


@app.get("/")
def home():
    return {
        "message": "Welcome to PackCheck AI-ML",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/analyze")
def analyze(data: LabelData):
    result = analyze_label(data.model_dump())
    return result

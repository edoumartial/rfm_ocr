from fastapi import FastAPI
from app.api.v1.api_router import router as api_router

app = FastAPI(title="RFM OCR API", version="1.0")

# Inclusion du routeur centralisé
app.include_router(api_router, prefix="/api/v1")
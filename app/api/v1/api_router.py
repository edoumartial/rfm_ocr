from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.ocr_service import process_pdf
import shutil
import os

router = APIRouter()

@router.post("/ocr/upload")
async def upload_and_process_ocr(file: UploadFile = File(...)):
    temp_file_path = f"temp_{file.filename}"
    try:
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = process_pdf(temp_file_path)
        
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])

        return {
            "message": "Traitement OCR réussi",
            "filename": file.filename,
            "data": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
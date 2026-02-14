from fastapi import APIRouter, UploadFile, File

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()

    return {
        "filename": file.filename,
        "size_in_bytes": len(content),
        "message": "File uploaded successfully."
    }
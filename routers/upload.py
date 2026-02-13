#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import APIRouter, UploadFile, File
from services.rag_service import process_document

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):
    result = await process_document(file)
    return {"status": "Document processed", "details": result}


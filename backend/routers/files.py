from fastapi import APIRouter, File, UploadFile, Depends
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # 파일 업로드 로직 (예: 저장, 유출 감지)
    file_content = await file.read()
    
    # 유출 감지 (예: 금지된 키워드 검사)
    forbidden_keywords = ["password", "confidential"]
    for keyword in forbidden_keywords:
        if keyword in file_content.decode("utf-8"):
            return {"status": "blocked", "message": "유출 위험 있는 파일"}
    
    # 파일 저장 로직 추가 필요
    return {"status": "success", "filename": file.filename}


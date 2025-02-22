from fastapi import APIRouter

router = APIRouter()
router = APIRouter(prefix="/logs")

@router.get("/activity")
async def get_activity_logs():
    # 로그 데이터를 가져오는 로직
    return {"message": "Activity logs here"}

@router.get("/security")
async def get_security_logs():
    # 보안 로그 데이터를 가져오는 로직
    return {"message": "Security logs here"}

@router.delete("/clear")
async def clear_logs():
    # 로그를 삭제하는 로직
    return {"message": "Logs cleared"}

from fastapi import APIRouter

router = APIRouter()

@router.get("/policies/")
def get_policies():
    return {"message": "Policy List"}
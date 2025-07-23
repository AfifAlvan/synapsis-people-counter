from fastapi import APIRouter

router = APIRouter()

@router.get("/api/stats/")
def get_stats():
    return {"message": "Ini data stats"}

@router.get("/api/stats/live")
def get_live():
    return {"message": "Ini data live"}

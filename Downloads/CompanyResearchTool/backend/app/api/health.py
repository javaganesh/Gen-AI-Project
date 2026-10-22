from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "Company Research Tool"
    }
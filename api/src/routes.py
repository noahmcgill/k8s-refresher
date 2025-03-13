from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v1", tags=["v1"])

@api_router.get("/")
def read_root():
    return {"Hello": "World"}

from fastapi import APIRouter, HTTPException

from ..main import connection_success

router = APIRouter(prefix="/api", tags=["System Checks"])


@router.get("/health-check")
async def health_check():
    try:
        status_message = "Server is up and running"

        return status_message
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/test-db-connection")
async def db_connection():
    return connection_success


@router.post("/test-db-connection")
async def db_connection():
    return connection_success

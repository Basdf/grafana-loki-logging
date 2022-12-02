from fastapi import APIRouter

from app.api.router import (
    root,
)


api_router = APIRouter()

api_router.include_router(root.router, prefix="/health-check")


from fastapi import APIRouter, Depends

from server.api.endpoints.detect import detect_router

router = APIRouter()
router.include_router(detect_router,
                      prefix="/api")

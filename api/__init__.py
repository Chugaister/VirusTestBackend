from fastapi import APIRouter
from api.system.system import system_router

router = APIRouter(prefix="/v1")
router.include_router(system_router, prefix="/system")

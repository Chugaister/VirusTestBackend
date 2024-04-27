from fastapi import APIRouter
from api.system.system import system_router
from api.users.users import users_router
from api.helprequests.helprequests import help_requests_router


router = APIRouter(prefix="/v1")
router.include_router(system_router, prefix="/system")
router.include_router(users_router, prefix="/users")
router.include_router(help_requests_router, prefix="/help-requests")

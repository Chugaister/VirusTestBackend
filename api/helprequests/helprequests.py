from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query
from pydantic import PositiveInt

from controllers.helprequests import HelpRequestController
from schemas.requests.helprequests import CreateHelpRequestRequest
from schemas.responses.helprequests import HelpRequestList
from schemas.responses.helprequests import HelpRequestResponse
from database.models.user import User
from utils.dependencies import get_current_user
from controllers.factory import ControllersFactory

help_requests_router = APIRouter(tags=["Help-requests"])


@help_requests_router.post("/")
async def create_help_request(
        help_request_request: CreateHelpRequestRequest,
        current_user: User = Depends(get_current_user),
        help_requests_controller: HelpRequestController = Depends(ControllersFactory.get_help_requests_controller)
) -> HelpRequestResponse:
    return await help_requests_controller.create_help_request(
        user=current_user,
        title=help_request_request.title,
        text=help_request_request.text,
        extra_text=help_request_request.extra_text,
        phone_number=help_request_request.phone_number,
        is_volunteer=help_request_request.is_volunteer
    )


@help_requests_router.get("/")
async def help_requests_search(
        limit: PositiveInt = Query(default=5),
        offset: PositiveInt = Query(default=0),
        help_requests_controller: HelpRequestController = Depends(ControllersFactory.get_help_requests_controller)
) -> HelpRequestList:
    items, size, total = await help_requests_controller.search_help_requests(
        None,
        limit=limit,
        offset=offset
    )
    return HelpRequestList(
        items=items,
        size=size,
        total=total
    )


@help_requests_router.get("/mine")
async def help_requests_by_user(
        current_user: User = Depends(get_current_user),
        limit: PositiveInt = Query(default=5),
        offset: PositiveInt = Query(default=0),
        help_requests_controller: HelpRequestController = Depends(ControllersFactory.get_help_requests_controller)
) -> HelpRequestList:
    items, size, total = await help_requests_controller.search_help_requests(
        user_id=current_user.user_id,
        limit=limit,
        offset=offset
    )
    return HelpRequestList(
        items=items,
        size=size,
        total=total
    )



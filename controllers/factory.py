from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import get_session

from controllers.users import UsersController
from controllers.helprequests import HelpRequestController


class ControllersFactory:

    @staticmethod
    def get_users_controller(session: AsyncSession = Depends(get_session)) -> UsersController:
        return UsersController(session)

    @staticmethod
    def get_help_requests_controller(session: AsyncSession = Depends(get_session)) -> HelpRequestController:
        return HelpRequestController(session)

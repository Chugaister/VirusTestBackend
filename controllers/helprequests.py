from sqlalchemy.ext.asyncio import AsyncSession
from controllers.base import BaseController
from typing import List
from typing import Tuple
from typing import Optional

from repositories.helprequests import HelpRequestsRepository
from database.models.user import User
from database.models.helprequest import HelpRequest


class HelpRequestController(BaseController):

    def __init__(self, session: AsyncSession):
        self.session = session
        self.hr_repo = HelpRequestsRepository()

    async def create_help_request(
            self,
            user: User,
            title: str,
            text: str,
            extra_text: str,
            phone_number: str,
            is_volunteer: bool,
    ) -> HelpRequest:
        hr = await self.hr_repo.create(
            self.session,
            attributes={
                "title": title,
                "text": text,
                "extra_text": extra_text,
                "phone_number": phone_number,
                "is_volunteer": is_volunteer,
                "user_id": user.user_id,
            }
        )
        await self.session.commit()
        return hr

    async def search_help_requests(
            self,
            user_id: Optional[int],
            limit: int,
            offset: int
    ) -> Tuple[List[HelpRequest], int, int]:
        hrs = await self.hr_repo.get_all_date_sorted(
            self.session,
            user_id,
            limit,
            offset
        )
        total = len(await self.hr_repo.get_all(self.session))
        return hrs, len(hrs), total

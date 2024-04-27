from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import desc
from repositories.base import BaseRepository
from database.models.helprequest import HelpRequest


class HelpRequestsRepository(BaseRepository):

    def __init__(self):
        super().__init__(HelpRequest)

    async def get_all_date_sorted(
            self,
            session: AsyncSession,
            user_id: int,
            limit: int,
            offset: int
    ) -> List[HelpRequest]:
        query = self.query()
        if user_id:
            query = query.where(HelpRequest.user_id == user_id)
        query = query.order_by(desc(HelpRequest.created_at)).limit(limit).offset(offset)
        return await self.all(session, query)

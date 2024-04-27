from pydantic import BaseModel
from pydantic import Field
from pydantic import ConfigDict
from schemas.base.helprequests import HelpRequestBase
from schemas.responses.users import UserResponse
from datetime import datetime
from typing import List


class HelpRequestResponse(HelpRequestBase):
    help_request_id: int = Field(example=123)
    created_at: datetime = Field(example="2024-04-27T16:20:00.000000Z")
    user: UserResponse

    model_config = ConfigDict(from_attributes=True)


class HelpRequestList(BaseModel):
    items: List[HelpRequestResponse]
    size: int = Field(example=10)
    total: int = Field(example=1348)

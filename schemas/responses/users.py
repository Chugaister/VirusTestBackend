from pydantic import BaseModel
from pydantic import Field
from pydantic import ConfigDict
from typing import Optional
from schemas.base.users import UserBase


class UserResponse(UserBase):
    user_id: int = Field(example=1203)

    model_config = ConfigDict(from_attributes=True)


class TokenResponse(BaseModel):
    token: Optional[str] = Field(default=None)


class UserRegisteredResponse(UserResponse, TokenResponse):
    pass

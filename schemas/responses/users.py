from pydantic import BaseModel
from pydantic import Field
from typing import Optional
from schemas.base.users import UserBase


class UserResponse(UserBase):
    user_id: int = Field(example=1203)


class TokenResponse(BaseModel):
    token: Optional[str] = Field(default=None)


class UserRegisteredResponse(UserResponse, TokenResponse):
    pass

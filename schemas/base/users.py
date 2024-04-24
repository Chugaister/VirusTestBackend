from pydantic import BaseModel
from pydantic import Field
from typing import Optional
from enum import Enum


class UserRole(str, Enum):
    requester = "requester"
    executor = "executor"


class UserBase(BaseModel):
    first_name: str = Field(example="John")
    last_name: Optional[str] = Field(example="Doe")
    phone_number: str = Field(example="+380000000000")
    role: UserRole = Field(examples=[UserRole.requester, UserRole.executor])

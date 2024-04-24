from pydantic import BaseModel
from pydantic import Field
from schemas.base.users import UserBase


class RegisterUserRequest(UserBase):
    password: str = Field(example="pass1234")


class LoginUserRequest(BaseModel):
    phone_number: str = Field(example="+380000000000")
    password: str = Field(example="pass1234")

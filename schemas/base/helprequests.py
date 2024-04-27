from pydantic import BaseModel
from pydantic import Field
from pydantic import constr
from typing import Optional


class HelpRequestBase(BaseModel):
    title: constr(max_length=128) = Field(
        example="Example caption"
    )
    text: constr(max_length=4096) = Field(
        example="Detailed text about help request"
    )
    extra_text: Optional[constr(max_length=1024)] = Field(
        default=None,
        example="Some text",
        description="I've no fucking idea what this text field is for"
    )
    phone_number: constr(max_length=16) = Field(
        example="+380000000000"
    )
    is_volunteer: bool = Field(default=False)

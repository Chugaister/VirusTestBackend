from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Enum

from database.base import Base
from database.mixins.timestamp import TimestampMixin

UserRole = Enum(
    "requester",
    "executor",
    name="user_role"
)


class User(Base, TimestampMixin):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    phone_number = Column(String, nullable=False)
    role = Column(UserRole)
    password_hash = Column(String, nullable=False)

    id_field_name = "user_id"


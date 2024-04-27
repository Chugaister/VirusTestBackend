from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship
from database.mixins.timestamp import TimestampMixin
from database.base import Base


class HelpRequest(Base, TimestampMixin):
    __tablename__ = "help_requests"
    help_request_id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    text = Column(String(4096), nullable=False)
    extra_text = Column(String(1024), nullable=True)
    phone_number = Column(String(16), nullable=False)
    is_volunteer = Column(Boolean, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    user = relationship("User", lazy="selectin")


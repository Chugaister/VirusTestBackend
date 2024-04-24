from sqlalchemy.ext.asyncio import AsyncSession
from controllers.base import BaseController
from typing import Tuple

from schemas.base.users import UserRole
from repositories.users import UsersRepository
from database.models.user import User
from exceptions.base import UnauthorizedException
from exceptions.base import BadRequestException
from utils.password import PasswordHandler
from utils.security import JWTHandler


class UsersController(BaseController):

    def __init__(self, session: AsyncSession):
        self.session = session
        self.user_repo = UsersRepository()

    async def register_user(
            self,
            first_name: str,
            last_name: str,
            phone_number: str,
            role: UserRole,
            password: str
    ) -> Tuple[User, str]:
        user: User = await self.user_repo.get_by(self.session, "phone_number", phone_number, unique=True)
        if user:
            raise BadRequestException("User already registered")
        password_hash = PasswordHandler.hash(password)
        user = await self.user_repo.create(
            self.session,
            attributes={
                "first_name": first_name,
                "last_name": last_name,
                "phone_number": phone_number,
                "role": role,
                "password_hash": password_hash
            }
        )
        token = await self.login_user(phone_number, password)
        await self.session.commit()
        return user, token

    async def login_user(
            self,
            phone_number: str,
            password: str
    ) -> str:
        user: User = await self.user_repo.get_by(self.session, "phone_number", phone_number, unique=True)
        if not user:
            raise UnauthorizedException("Invalid credentials")
        if not PasswordHandler.verify(user.password_hash, password):
            raise UnauthorizedException("Invalid credentials")
        token = JWTHandler.encode(payload={"user_id": user.user_id}, type_="access")
        return token


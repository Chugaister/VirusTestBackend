from fastapi import APIRouter
from fastapi import Depends
from schemas.requests.users import RegisterUserRequest
from schemas.requests.users import LoginUserRequest
from schemas.responses.users import UserResponse
from schemas.responses.users import UserRegisteredResponse
from schemas.responses.users import TokenResponse

from controllers.users import UsersController
from controllers.factory import ControllersFactory
from database.models.user import User
from utils.dependencies import get_current_user

users_router = APIRouter(tags=["Authentication"])


@users_router.post("/register")
async def register_user(
        register_user_request: RegisterUserRequest,
        users_controller: UsersController = Depends(ControllersFactory.get_users_controller)
) -> UserRegisteredResponse:
    user, token = await users_controller.register_user(
        register_user_request.first_name,
        register_user_request.last_name,
        register_user_request.phone_number,
        register_user_request.role,
        register_user_request.password
    )
    response = UserRegisteredResponse.model_validate(user, from_attributes=True, context={"token": token})
    response.token = token
    return response


@users_router.post("/login")
async def login(
        login_user_request: LoginUserRequest,
        users_controller: UsersController = Depends(ControllersFactory.get_users_controller)
) -> TokenResponse:
    token = await users_controller.login_user(
        login_user_request.phone_number,
        login_user_request.password
    )
    return TokenResponse(token=token)


@users_router.post("/me")
async def login(
        user: User = Depends(get_current_user)
) -> UserResponse:
    return user

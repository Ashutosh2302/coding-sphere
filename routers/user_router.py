from fastapi import APIRouter, status
from typing import List
from models.user import RegisterUserRequest, LoginUserRequest, LoginUserResponse
from database.users import register, login

router = APIRouter()


@router.post("/login", response_description="Login User", status_code=status.HTTP_201_CREATED) 
async def login_user_handler(user: LoginUserRequest) -> LoginUserResponse:
    return await login(user)

@router.post("/register", response_description="Register User", status_code=status.HTTP_201_CREATED) 
async def register_user_handler(user: RegisterUserRequest) -> dict:
    return await register(user)

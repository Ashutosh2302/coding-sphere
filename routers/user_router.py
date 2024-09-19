from fastapi import APIRouter, status, Depends
from typing import List
from models.user import RegisterUserRequest, LoginUserResponse
from database.users import register, login
from fastapi.security import OAuth2PasswordRequestForm
from utils.error_respones import login_error_responses, register_error_responses
router = APIRouter()


@router.post("/login", response_description="Login User", status_code=status.HTTP_201_CREATED, responses=login_error_responses) 
async def login_user_handler(user: OAuth2PasswordRequestForm = Depends(),) -> LoginUserResponse:
    return await login(user)

@router.post("/register", response_description="Register User", status_code=status.HTTP_201_CREATED, responses=register_error_responses) 
async def register_user_handler(user: RegisterUserRequest) -> dict:
    return await register(user)

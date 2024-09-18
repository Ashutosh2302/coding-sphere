from models.user import RegisterUserRequest, User, IUser, LoginUserRequest, LoginUserResponse
from fastapi import HTTPException
from mongoengine import DoesNotExist
from mongoengine import ValidationError, NotUniqueError
from utils.jwt import create_access_token
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def get_user_by_username(username: str) -> IUser:
  try:
    user = User.objects.get(username=username)
    return {"id": str(user.id), "username": user.username, "password": user.password, "role": user.role}
      
  except DoesNotExist:
        raise HTTPException(status_code=400, detail="User not found")
  
  except Exception as e:
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")


async def login(u: LoginUserRequest) -> LoginUserResponse:
  user = await get_user_by_username(u.username)
  try:
    if not pwd_context.verify(u.password, user.get("password")):
         raise HTTPException(status_code=401, detail="Invalid password")
    token = create_access_token({"id": user.get("id"), "username": user.get("username"), "role": user.get("role")}, 1)
    return {"access_token": token}

  except HTTPException as e:
    raise e
    
  except Exception as e:
    print(f"Unexpected error: {e}")
    raise HTTPException(status_code=500, detail="An unexpected error occurred")


async def register(user: RegisterUserRequest) -> dict:
    try: 
        hashed_password = pwd_context.hash(user.password)
        created_user = User(username=user.username, password=hashed_password, role=user.role).save()
        if created_user:
            return {"detail": "User registration successful, Please login!!"}
    
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=f"Validation error: {e}")

    except NotUniqueError:
        raise HTTPException(status_code=400, detail="Username not available")

    except Exception as e:
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

import jwt
import os
from datetime import datetime, timedelta, timezone
from models.user import Role, TokenData
from fastapi.security import OAuth2PasswordBearer
import jwt 
import os
from jwt.exceptions import InvalidTokenError
from fastapi import status, Depends, HTTPException 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def create_access_token(user: dict, hours: float) -> str:
    expire = datetime.now(timezone.utc) + timedelta(hours=hours)
    return jwt.encode({"id": user.get("id"), "username":  user.get("username"), "role":  "user" if user.get("role") == Role.USER else "admin",  "exp": expire}, os.getenv("SECRET_KEY"), algorithm="HS256")


credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token",
        headers={"WWW-Authenticate": "Bearer"},
    )

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
        id: str = payload.get("id")
        username: str = payload.get("username")
        role: str = payload.get("role")
        if id is None or username is None or role is None:
            print("chhhhcutie")
            raise credentials_exception
    except InvalidTokenError as e:
        print("chhhh", e)
        raise credentials_exception

    return TokenData(id=id, username=username, role=role)


def admin_required(user: TokenData = Depends(verify_token)):
    if user.role != Role.ADMIN:
            raise HTTPException(
                status_code=403,
                detail="Insufficient permissions",
            )

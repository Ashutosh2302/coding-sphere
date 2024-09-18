from enum import Enum
from pydantic import BaseModel
from mongoengine import Document, StringField, EnumField


class Role(Enum):
    ADMIN = 'admin'
    USER = 'user'
    
class User(Document):
    username = StringField(max_length=50, required=True)
    password = StringField(max_length=250, required=True)
    role = EnumField(Role, default=Role.USER)
    meta = {
        'collection': 'user',
        'indexes': [
             {"fields": ["username",],
            "unique": True,
         }
        ]
    }
  
class IUser(BaseModel):
   id: str
   username: str
   password: str
   role: Role
   
class RegisterUserRequest(BaseModel):
    username: str
    password: str
    role: Role | None = Role.USER


class LoginUserRequest(BaseModel):
    username: str
    password: str

class LoginUserResponse(BaseModel):
   access_token: str


class TokenData(BaseModel):
   id: str
   username: str
   role: Role

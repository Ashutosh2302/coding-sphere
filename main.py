

from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from routers.project_router import router as project_router
from routers.user_router import router as user_router
from contextlib import asynccontextmanager
from database.db import init_db, close_db

app = FastAPI()


@asynccontextmanager
async def lifespan():
    init_db()
    yield
    close_db()


@app.get("/")
async def read_root():
    return {"message": "API is healthy"}


app.include_router(project_router, tags=["projects"], prefix="/projects")
app.include_router(user_router, tags=["users"], prefix="/users")

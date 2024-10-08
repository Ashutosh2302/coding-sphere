from fastapi import APIRouter, status, Depends 
from typing import List
from models.project import ProjectResponse, ProjectCreate, ProjectUpdate
from database.projects import get_projects, create_project_db, update_project_db, get_project, delete_project_db
from utils.jwt import verify_token, admin_required
from utils.error_respones import get_project_error_respones, get_projects_error_respones, create_project_error_respones, update_project_error_respones, delete_project_error_respones

router = APIRouter(dependencies=[Depends(verify_token)] )

@router.get("/", response_description="Get all Projects", responses=get_projects_error_respones) 
async def list_projects() -> List[ProjectResponse]:
    return await get_projects()


@router.get("/{id}", response_description="Get project by Id", responses=get_project_error_respones) 
async def list_project(id: str) -> ProjectResponse:
    return await get_project(id)


@router.post("/", response_description="Create Project", status_code=status.HTTP_201_CREATED, responses=create_project_error_respones) 
async def create_project(project: ProjectCreate, _ = Depends(admin_required)) -> ProjectResponse:
    return await create_project_db(project)


@router.patch("/{id}", response_description="Update Project", status_code=status.HTTP_200_OK, responses=update_project_error_respones) 
async def update_project(id: str, project: ProjectUpdate, _ = Depends(admin_required)) -> ProjectResponse:
    return await update_project_db(id, project)


@router.delete("/{id}", response_description="Delete Project", status_code=status.HTTP_200_OK, responses=delete_project_error_respones) 
async def delete_project(id: str, _ = Depends(admin_required)):
    return await delete_project_db(id)

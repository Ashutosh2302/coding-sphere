from models.project import Project, ProjectCreate, ProjectResponse, ProjectUpdate
from typing import List
from fastapi import HTTPException
from mongoengine import DoesNotExist
from mongoengine import ValidationError, NotUniqueError


async def get_project(id: str) -> ProjectResponse:
  try:
    project = Project.objects.get(id=id)
    return {"id": str(project.id), "name": project.name, "description": project.description} 
  
  except DoesNotExist:
        raise HTTPException(status_code=400, detail="Project not found")
  
  except Exception as e:
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")


async def get_projects() -> List[ProjectResponse]:
  try:
    projects = Project.objects()
    return [{"id": str(project.id), "name": project.name, "description": project.description} for project in projects]
  
  except Exception as e:
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")


async def create_project_db(project: ProjectCreate) -> ProjectResponse:
    try: 
        created_project = Project(name=project.name, description=project.description).save()
        return {"id": str(created_project.id), "name": created_project.name, "description": created_project.description}
    
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=f"Validation error: {e}")

    except NotUniqueError:
        raise HTTPException(status_code=400, detail="A project with this name already exists")

    except Exception as e:
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")


async def update_project_db(id: str, project: ProjectUpdate) -> ProjectResponse:
    try:
        result = Project.objects(id=id).update_one(**project.model_dump(exclude_unset=True))
        if result == 0:
            raise HTTPException(status_code=400, detail="Project not found")
        
    except HTTPException as e:
        raise e
    
    except NotUniqueError:
        raise HTTPException(status_code=400, detail="A project with this name already exists")

    except Exception as e:
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

    return await get_project(id)


async def delete_project_db(id: str):
    try:
        result = Project.objects(id=id).delete()
        if result == 0:
            raise HTTPException(status_code=400, detail="Project not found")
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

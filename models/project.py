from pydantic import BaseModel, Field
from mongoengine import Document, StringField

class Project(Document):
    name = StringField(max_length=100, required=True)
    description = StringField(max_length=500, required=True)
    meta = {
        'collection': 'projects',
        'indexes': [
             {"fields": ["name",],
            "unique": True,
         }
        ]
    }
  

class ProjectCreate(BaseModel):
    name: str
    description: str

class ProjectResponse(BaseModel):
    id: str
    name: str
    description: str

class ProjectUpdate(BaseModel):
    name: str | None = Field(default=None,  title="The name of the project", max_length=100)
    description: str | None = Field(default=None,  title="The description of the project", max_length=500)

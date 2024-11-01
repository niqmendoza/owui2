from pydantic import BaseModel

class GroupBase(BaseModel):
    name: str

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int
    class Config:
        orm_mode = True

class GroupAssignModel(BaseModel):
    model_id: int
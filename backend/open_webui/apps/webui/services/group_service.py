from sqlalchemy.orm import Session
from ..models import Group
from ..models import Model
from ..schemas import GroupCreate

def create_group(db: Session, group: GroupCreate):
    db_group = Group.create(name=group.name)
    return db_group

def assign_model_to_group(db: Session, group_id: int, model_id: int):
    group = Group.get(Group.id == group_id)
    model = Model.get(Model.id == model_id)
    if group and model:
        group.model_id = model_id
        group.save()
        return group
    return None
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..internal.db import get_db  #g
from ..services.group_service import create_group, assign_model_to_group #corrigeme la rutapue
from ..schemas import GroupCreate, GroupAssignModel, Group  # Ruta corregida para schemas

router = APIRouter()

@router.post("/groups/", response_model=Group)
def create_group_endpoint(group: GroupCreate, db: Session = Depends(get_db)):
    return create_group(db=db, group=group)

@router.post("/groups/{group_id}/assign_model", response_model=Group)
def assign_model_to_group_endpoint(group_id: int, model_id: int, db: Session = Depends(get_db)):
    return assign_model_to_group(db=db, group_id=group_id, model_id=model_id)

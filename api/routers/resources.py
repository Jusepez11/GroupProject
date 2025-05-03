from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..schemas.resources import ResourceCreate, ResourceUpdate, Resource
from ..controllers import resources

router = APIRouter()

@router.post("/resources", response_model=Resource)
def create_resource(request: ResourceCreate, db: Session = Depends(get_db)):
    return resources.create(db, request)

@router.get("/resources", response_model=list[Resource])
def get_all_resources(db: Session = Depends(get_db)):
    return resources.read_all(db)

@router.get("/resources/{resource_id}", response_model=Resource)
def get_resource(resource_id: int, db: Session = Depends(get_db)):
    return resources.read_one(db, resource_id)

@router.put("/resources/{resource_id}", response_model=Resource)
def update_resource(resource_id: int, request: ResourceUpdate, db: Session = Depends(get_db)):
    return resources.update(db, resource_id, request)

@router.delete("/resources/{resource_id}")
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    return resources.delete(db, resource_id)
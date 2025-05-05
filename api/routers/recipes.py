from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.recipe import RecipeCreate, RecipeUpdate, RecipeRead
from api.controllers import recipe as controller
from api.dependencies.database import get_db

router = APIRouter(prefix="/recipes", tags=["Recipes"])

@router.post("/", response_model=RecipeRead)
def create_recipe(request: RecipeCreate, db: Session = Depends(get_db)):
    return controller.create_recipe(db, request)

@router.get("/", response_model=list[RecipeRead])
def read_all_recipes(db: Session = Depends(get_db)):
    return controller.read_all_recipes(db)

@router.get("/{recipe_id}", response_model=RecipeRead)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return controller.read_recipe(db, recipe_id)

@router.put("/{recipe_id}", response_model=RecipeRead)
def update_recipe(recipe_id: int, request: RecipeUpdate, db: Session = Depends(get_db)):
    return controller.update_recipe(db, recipe_id, request)

@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return controller.delete_recipe(db, recipe_id)

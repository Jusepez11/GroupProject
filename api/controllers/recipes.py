from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError
from ..models import recipe as model
from ..schemas.recipe import RecipeCreate, RecipeUpdate


def create_recipe(db: Session, request: RecipeCreate):
    new_recipe = model.Recipe(
        amount=request.amount
    )
    try:
        db.add(new_recipe)
        db.commit()
        db.refresh(new_recipe)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return new_recipe


def read_all_recipes(db: Session):
    try:
        return db.query(model.Recipe).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def read_recipe(db: Session, recipe_id: int):
    try:
        recipe = db.query(model.Recipe).filter(model.Recipe.id == recipe_id).first()
        if not recipe:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe ID not found.")
        return recipe
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def update_recipe(db: Session, recipe_id: int, request: RecipeUpdate):
    try:
        recipe_query = db.query(model.Recipe).filter(model.Recipe.id == recipe_id)
        if not recipe_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe ID not found.")
        update_data = request.dict(exclude_unset=True)
        recipe_query.update(update_data, synchronize_session=False)
        db.commit()
        return recipe_query.first()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def delete_recipe(db: Session, recipe_id: int):
    try:
        recipe_query = db.query(model.Recipe).filter(model.Recipe.id == recipe_id)
        if not recipe_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe ID not found.")
        recipe_query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

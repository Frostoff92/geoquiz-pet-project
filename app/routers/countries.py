from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import Country
from app.services.quiz_service import (
    get_all_countries,
    get_country_by_id,
)


router = APIRouter(
    prefix="/countries",
    tags=["Countries"]
)


@router.get("", response_model=list[Country])
def countries(db: Session = Depends(get_db)):
    return get_all_countries(db)


@router.get("/{country_id}", response_model=Country)
def country_by_id(country_id: int, db: Session = Depends(get_db)):
    return get_country_by_id(db, country_id)
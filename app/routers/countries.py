from fastapi import APIRouter

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
def countries():
    return get_all_countries()


@router.get("/{country_id}", response_model=Country)
def country_by_id(country_id: int):
    return get_country_by_id(country_id)
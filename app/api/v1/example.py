from fastapi import APIRouter
from app.core.presenter import example as example_presenter
from dataclasses import asdict

router = APIRouter()


@router.get('/example')
async def root():
    return asdict(await example_presenter.display_data())

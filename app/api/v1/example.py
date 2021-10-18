from fastapi import APIRouter
from app.core.presenter import example

router = APIRouter()


@router.get('/example')
async def root():
    return (await example.display_data()).toDict()

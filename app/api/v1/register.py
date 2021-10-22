from fastapi import APIRouter
from app.core.presenter import register as register_presenter
from app.core.model import register as register_model
from dataclasses import asdict

router = APIRouter()


@router.post('/register')
async def root(user: register_model.User):
    return await register_presenter.handle_register(user)

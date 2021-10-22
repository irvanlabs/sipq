from fastapi import APIRouter
from app.core.model import register as register_model

router = APIRouter()


@router.post("/register")
async def handle_register(user: register_model.User) -> register_model.Result:
    return register_model.Result(
        user_id='xxx',
        signature='yyy',
    )

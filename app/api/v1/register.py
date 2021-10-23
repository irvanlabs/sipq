from fastapi import APIRouter
from app.core.presenter import register as register_p
from app.core.model import register as register_m

router = APIRouter()


@router.post('/register')
async def root(data_diri: register_m.DataDiri):
    return await register_p.handle(data_diri)

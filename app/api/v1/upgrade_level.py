from fastapi import APIRouter
from app.core.model import upgrade_level as upgrade_level_model

router = APIRouter()


@router.post('/upgrade_level')
async def root(params: upgrade_level_model.Upgrade):
    return await upgrade_level_presenter.handle_upgrade_level(params)

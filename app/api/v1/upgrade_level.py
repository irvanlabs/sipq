from fastapi import APIRouter
from app.core.presenter import upgrade_level as upgrade_level_pres
from app.core.model import upgrade_level as upgrade_level_mod

router = APIRouter()


@router.post('/level/upgrade', response_model=upgrade_level_mod.Result)
async def upgrade_level(user_id: str, level_now: upgrade_level_mod.Level, target_level: upgrade_level_mod.Level) -> upgrade_level_mod.Result:
    return await upgrade_level_pres.handle(user_id, level_now, target_level)

@router.get('/level')
async def list_level():
    list_levels = {
    "administrator":[{"kode_level":1}],
    "admin_pusat":[{"kode_level":2}],
    "admin_provinsi":[{"kode_level":3}],
    "admin_kabupaten":[{"kode_level":4}],
    "caleg":[{"kode_level":5}],
    "saksi":[{"kode_level":6}],
    "anggota":[{"kode_level":7}],
    }

    return list_levels
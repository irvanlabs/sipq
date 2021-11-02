from fastapi import APIRouter
from app.core.presenter import level as level_pres
from app.core.model import level as level_mod

router = APIRouter()

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

@router.post('/level/upgrade')
async def upgrade_level(upgrade: level_mod.UpgradeLevel):
    return await level_pres.handle(upgrade.user_id, upgrade.user_id_target, upgrade.target_level, mode='upgrade')

@router.post('/level/downgrade',)
async def downgrade_level(user_id: int, user_id_target: int, target_level: level_mod.Level, mode = 'downgrade') -> level_mod.Result:
    return await level_pres.handle(user_id, user_id_target, target_level, mode)

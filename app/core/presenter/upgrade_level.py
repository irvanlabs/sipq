from app.core.model import upgrade_level as upgrade_level_mod

async def handle(user_id: str, level_now: upgrade_level_mod.Level, target_level: upgrade_level_mod.Level) -> upgrade_level_mod.Result:
	return await upgrade_level_mod.upgrade_to_new_level(user_id, level_now, target_level)
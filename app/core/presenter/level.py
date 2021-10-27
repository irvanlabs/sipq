from app.core.model import level as level_mod

async def handle(user_id: str, user_id_target: str, target_level: level_mod.Level, mode = None) -> level_mod.Result:
	return await level.update_level(user_id, user_id_target, target_level, mode)

# async def handle_downgrade(user_id: str, user_id_target: upgrade_level_mod.Level, target_level: upgrade_level_mod.Level) -> upgrade_level_mod.Result:
# 	return await upgrade_level_mod.upgrade_level(user_id, user_id_target, target_level)
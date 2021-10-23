from app.core.model import register as register_m


async def handle(data_diri: register_m.DataDiri) -> register_m.Result:
    return await register_m.insert_new_data_diri(data_diri)

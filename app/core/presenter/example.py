from app.core.model import example


async def display_data() -> example.Data:
    return await example.get_data()

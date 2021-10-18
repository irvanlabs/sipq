from app.core.model import example as example_model


async def display_data() -> example_model.Data:
    return await example_model.get_data()

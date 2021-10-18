from dataclasses import dataclass


@dataclass
class Data:
    name: str = 'Jhon Doe'
    age: int = 39
    weight: int = 52


async def get_data() -> Data:
    return Data()

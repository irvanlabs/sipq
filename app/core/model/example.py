from dataclasses import dataclass


@dataclass
class Data:
    name = 'Jhon Doe'
    age = 39
    weight = 52

    def toDict(self):
        return {
            'name': self.name,
            'age': self.age,
            'weight': self.weight,
        }


async def get_data() -> Data:
    return Data()

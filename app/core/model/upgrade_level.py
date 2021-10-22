from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum


class Level(int, Enum):
    administrator: int = 1
    admin_pusat: int = 2
    admin_provinsi: int = 3
    admin_kabupaten: int = 4
    caleg: int = 5
    saksi: int = 6
    anggota: int = 7


class Upgrade(BaseModel):
    user_id: str
    target_id: str
    target_level: Level

    def __init__(self, user_id: str, target_id: str, target_level: int):
        if (type(user_id) is not str or len(user_id) < 1) or (
                type(target_id) is not str or
                len(target_id) < 1) or (target_level < 1 or target_level > 7):
            raise HTTPException(status_code=400)

        self.user_id = user_id
        self.target_id = target_id

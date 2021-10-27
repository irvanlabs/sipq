from pydantic import BaseModel
from fastapi import HTTPException
from typing import NamedTuple
from enum import Enum
from pymysql.connections import Connection
from pymysql.err import IntegrityError
from hashlib import sha512
from app.core import config


class Level(int, Enum):
    administrator: int = 1
    admin_pusat: int = 2
    admin_provinsi: int = 3
    admin_kabupaten: int = 4
    caleg: int = 5
    saksi: int = 6
    anggota: int = 7


class Result(BaseModel):
    user_id: str
    level_now: Level
    target_level: Level

    def __init__(self, user_id: str, level_now: Level, target_level: Level):
        self.user_id = user_id
        self.target_id = level_now
        self.target_level = target_level



async def update_level(user_id: str, user_id_target: str, target_level: Level, mode = None) -> Result:
    conn = Connection(
        user=config.DB_USER,
        password=config.DB_PASS,
        database=config.DB_NAME,
        # host='localhost',
    )

    # data_diri.hash = sha512(
    #     (data_diri.nama_lengkap + data_diri.nik).encode()).hexdigest()
    if mode == 'upgrade':
        update_query = '''

        '''
    elif mode == 'downgrade':
        update_query = '''

        '''
    else:
        return "mode is not acceptable"
        
    with conn:
        conn.begin()
        try:
            with conn.cursor() as cur:
                cur.execute(query=insert_query, args=data_diri.getDict())
            conn.commit()
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail='insert error, due to malformed request or wrong data')
            conn.rollback()
        else:
            conn.rollback()

    return Result(
        nama_lengkap=data_diri.nama_lengkap,
        hash=data_diri.hash,
        level=Level.anggota,
    )



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



async def upgrade_to_new_level(user_id: str, level_now: Level, target_level: Level) -> Result:
    conn = Connection(
        user=config.DB_USER,
        password=config.DB_PASS,
        database=config.DB_NAME,
        host='localhost',
    )

    # data_diri.hash = sha512(
    #     (data_diri.nama_lengkap + data_diri.nik).encode()).hexdigest()

    insert_query = '''
    -- INSERT INTO `data_diri` (nik,nama_lengkap,ttl,jenis_kelamin,status_perkawinan,pekerjaan,pendidikan_terakhir,alamat_lengkap,sosial_media,level,hash)
    -- VALUES (%(nik)s,%(nama_lengkap)s,%(ttl)s,%(jenis_kelamin)s,%(status_perkawinan)s,%(pekerjaan)s,%(pendidikan_terakhir)s,%(alamat_lengkap)s,%(sosial_media)s,7,%(hash)s)
    '''

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

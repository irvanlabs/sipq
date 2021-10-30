from pydantic import BaseModel
from fastapi import HTTPException
from typing import NamedTuple
from enum import Enum
from calendar import month_name
from pymysql.connections import Connection
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


class Gender(str, Enum):
    P = 'P'
    L = 'L'


class Ttl(NamedTuple):
    kota: str
    tanggal: int
    bulan: int
    tahun: int

    def __str__(self) -> str:
        return f"{self.kota}, {self.tanggal} {month_name[self.bulan]} {self.tahun}"


class DataDiri(BaseModel):
    nik: str
    nama_lengkap: str
    ttl: Ttl
    jenis_kelamin: Gender
    status_perkawinan: str
    pekerjaan: str
    pendidikan_terakhir: str
    alamat_lengkap: str
    email: str
    notelp: str
    hash: str
    level: Level = Level.anggota


class Result(BaseModel):
    nama_lengkap: str
    hash: str
    level: Level


async def insert_new_data_diri(data_diri: DataDiri) -> Result:
    data_diri.hash = sha512(data_diri.nik.encode()).hexdigest()
    # overwrite level
    data_diri.level = Level.anggota

    query = '''
    INSERT INTO `data_diri` (nik,nama_lengkap,ttl,jenis_kelamin,status_perkawinan,pekerjaan,pendidikan_terakhir,alamat_lengkap,email,notelp,hash,level)
    VALUES (%(nik)s,%(nama_lengkap)s,%(ttl)s,%(jenis_kelamin)s,%(status_perkawinan)s,%(pekerjaan)s,%(pendidikan_terakhir)s,%(alamat_lengkap)s,%(email)s,%(notelp)s,%(hash)s,%(level)s)
    '''

    conn = Connection(
        user=config.DB_USER,
        password=config.DB_PASS,
        database=config.DB_NAME,
        host=config.DB_HOST,
    )

    with conn:
        conn.begin()
        try:
            with conn.cursor() as cur:
                args = data_diri.dict()
                args['level'] = args['level'].value
                print(cur.mogrify(query=query, args=args))
                cur.execute(query=query, args=args)
        except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=400, detail=str(e))
        conn.commit()

    return Result(nama_lengkap=data_diri.nama_lengkap,
                  hash=data_diri.hash,
                  level=data_diri.level)

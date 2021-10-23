from pydantic import BaseModel
from fastapi import HTTPException
from typing import NamedTuple
from enum import Enum
from calendar import month_name
from datetime import datetime
from pymysql.connections import Connection
from pymysql.err import IntegrityError
from hashlib import sha512
from app.core import config


class Level(Enum):
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
    __id: int
    nik: str
    nama_lengkap: str
    ttl: Ttl
    jenis_kelamin: Gender
    status_perkawinan: str
    pekerjaan: str
    pendidikan_terakhir: str
    alamat_lengkap: str
    sosial_media: str
    __date_created: datetime
    __date_updated: datetime
    __level: Level
    hash: str

    def getDict(self):
        return {
            'nik': self.nik,
            'nama_lengkap': self.nama_lengkap,
            'ttl': str(self.ttl),
            'jenis_kelamin': self.jenis_kelamin,
            'status_perkawinan': self.status_perkawinan,
            'pekerjaan': self.pekerjaan,
            'pendidikan_terakhir': self.pendidikan_terakhir,
            'alamat_lengkap': self.alamat_lengkap,
            'sosial_media': self.sosial_media,
            'hash': self.hash,
            'level': Level.anggota
        }


class Result(BaseModel):
    nama_lengkap: str
    hash: str
    level: int

    def __init__(self, nama_lengkap: str, hash: str, level: int):
        self.nama_lengkap = nama_lengkap
        self.hash = hash
        self.level = level


async def insert_new_data_diri(data_diri: DataDiri) -> Result:
    conn = Connection(
        user=config.DB_USER,
        password=config.DB_PASS,
        database=config.DB_NAME,
        host='localhost',
    )

    data_diri.hash = sha512(
        (data_diri.nama_lengkap + data_diri.nik).encode()).hexdigest()

    insert_query = '''
    INSERT INTO `data_diri` (nik,nama_lengkap,ttl,jenis_kelamin,status_perkawinan,pekerjaan,pendidikan_terakhir,alamat_lengkap,sosial_media,level,hash)
    VALUES (%(nik)s,%(nama_lengkap)s,%(ttl)s,%(jenis_kelamin)s,%(status_perkawinan)s,%(pekerjaan)s,%(pendidikan_terakhir)s,%(alamat_lengkap)s,%(sosial_media)s,7,%(hash)s)
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

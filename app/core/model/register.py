from fastapi import FastAPI
from typing import Optional, NamedTuple
from pydantic import BaseModel
from enum import Enum
from calendar import month_name
from datetime import datetime
from dataclasses import dataclass


class Gender(str, Enum):
    P = 'P'
    L = 'L'


class Ttl(NamedTuple):
    kota: str
    tanggal: int
    bulan: int
    tahun: int

    def __str__(self) -> str:
        bulan_str = month_name[self.bulan]
        return "%s, %d %s %d".format(
            self.kota,
            self.tanggal,
            bulan_str,
            self.tahun,
        )


class User(BaseModel):
    __id: int
    __date_created: datetime
    __date_updated: datetime
    __level: int
    nik: str
    nama: str
    ttl: Ttl
    jenis_kelamin: Gender
    status_perkawinan: str
    pekerjaan: str
    alamat: str
    sosial_media: Optional[str]


@dataclass(init=True)
class Result:
    user_id: str
    signature: str

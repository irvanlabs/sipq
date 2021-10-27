from fastapi import HTTPException
from pydantic import BaseModel, validators
from enum import Enum
from datetime import datetime
from typing import Optional, List
from pymysql import Connection, cursors
from app.core import config
import logging
from app import lib


class BeritaStatus(int, Enum):
    unpublish: int = 0
    publish: int = 1


class SetBerita(BaseModel):
    user: str
    judul: str
    isi: str
    slug: str
    tag: str
    keyword: str
    kategori: List[int]


class GetBerita(BaseModel):
    user: Optional[int]
    judul: Optional[str]
    slug: Optional[List[str]]
    tag: Optional[List[str]]
    keyword: Optional[List[str]]
    status: Optional[BeritaStatus]
    kategori: Optional[List[int]]


async def set_berita(params: SetBerita):
    insert_query = '''
    INSERT INTO berita (user,judul,isi,slug,tag,keyword,kategori)
    VALUES (%(user)s,%(judul)s,%(isi)s,%(slug)s,%(tag)s,%(keyword)s,%(kategori)s)
    '''

    conn = Connection(user=config.DB_USER,
                      password=config.DB_PASS,
                      database=config.DB_NAME,
                      host=config.DB_HOST,
                      cursorclass=cursors.DictCursor)

    with conn:
        res = await lib.get_user_id(conn, params.user)
        if not res:
            raise HTTPException(
                status_code=400,
                detail='insert error, due to malformed request or wrong data')

        conn.begin()
        try:
            with conn.cursor() as cur:
                args = params.dict()
                args['user'] = res['id']
                args['kategori'] = ','.join([str(x) for x in args['kategori']])
                cur.execute(query=insert_query, args=args)
        except Exception as e:
            logging.error(e)
            conn.rollback()
            raise HTTPException(
                status_code=400,
                detail='insert error, due to malformed request or wrong data')
        conn.commit()


async def get_berita(params: GetBerita) -> List[GetBerita]:
    insert_query = '''
    INSERT INTO berita (judul,isi,slug,tag,keyword,kategori)
    VALUES (%(judul)s,%(isi)s,%(slug)s,%(tag)s,%(keyword)s,%(kategori)s)
    '''

    conn = Connection(user=config.DB_USER,
                      password=config.DB_PASS,
                      database=config.DB_NAME,
                      host=config.DB_HOST,
                      cursorclass=cursors.DictCursor)

    with conn:
        conn.begin()
        try:
            with conn.cursor() as cur:
                args = params.dict()
                args['kategori'] = ','.join([str(x) for x in args['kategori']])
                cur.execute(query=insert_query, args=args)
        except Exception as e:
            logging.error(e)
            conn.rollback()
            raise HTTPException(
                status_code=400,
                detail='insert error, due to malformed request or wrong data')
        conn.commit()

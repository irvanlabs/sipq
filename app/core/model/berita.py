from fastapi import HTTPException
from pydantic import BaseModel
from enum import Enum
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


async def set_berita(params: SetBerita):
    query = """
    INSERT INTO berita (user,judul,isi,slug,tag,keyword,kategori)
    VALUES (%(user)s,%(judul)s,%(isi)s,%(slug)s,%(tag)s,%(keyword)s,%(kategori)s)
    """
    db_config = config.get_db_config(online=False)
    conn = Connection(user=db_config['DB_USER'],
                      password=db_config['DB_PASS'],
                      database=db_config['DB_NAME'],
                      host=db_config['DB_HOST'],
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
                print(cur.mogrify(query=query, args=args))
                cur.execute(query=query, args=args)
        except Exception as e:
            logging.error(e)
            conn.rollback()
            raise HTTPException(status_code=400, detail=str(e))
        conn.commit()


class GetBerita(BaseModel):
    user: Optional[str]
    judul: Optional[str]
    slug: Optional[str]
    tag: Optional[str]
    keyword: Optional[str]
    status: Optional[BeritaStatus] = BeritaStatus.publish
    kategori: Optional[str]
    limit: Optional[int] = 100


async def get_berita(params: GetBerita) -> List[dict]:
    db_config = config.get_db_config(online=False)
    conn = Connection(user=db_config['DB_USER'],
                      password=db_config['DB_PASS'],
                      database=db_config['DB_NAME'],
                      host=db_config['DB_HOST'],
                      cursorclass=cursors.DictCursor)

    query = """SELECT judul,slug,tag,keyword,status,kategori FROM `berita`"""
    where = []

    user_id = None
    if params.user:
        where.append('user=%(user)s')
        uid = await lib.get_user_id(conn=conn, hash_value=params.user)
        if not uid or not uid.get('id'):
            raise HTTPException(
                status_code=400,
                detail='select error, due to malformed request or wrong data')
        user_id = uid['id']

    where.append('status=%(status)s')

    if params.judul:
        params.judul = f'%{params.judul}%'
        where.append('judul LIKE %(judul)s')

    if params.slug:
        params.slug = f'%{params.slug}%'
        where.append('slug LIKE %(slug)s')

    if params.tag:
        params.tag = f'%{params.tag}%'
        where.append('tag LIKE %(tag)s')

    if params.keyword:
        params.keyword = f'%{params.keyword}%'
        where.append('keyword LIKE %(keyword)s')

    if params.kategori:
        params.kategori = f'%{params.kategori}%'
        where.append('kategori LIKE %(kategori)s')

    query = f'{query} WHERE  {" AND ".join(where)}'
    query = f'{query} LIMIT %(limit)s'

    res = []

    with conn:
        conn.begin()
        try:
            with conn.cursor() as cur:
                args = params.dict()
                args['status'] = str(args['status'].value)
                args['user'] = user_id
                print(cur.mogrify(query=query, args=args))
                cur.execute(query=query, args=args)
                res = cur.fetchall()
        except Exception as e:
            logging.error(e)
            conn.rollback()
            raise HTTPException(status_code=400, detail=str(e))
        conn.commit()

    return res

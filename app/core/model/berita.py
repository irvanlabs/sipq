from fastapi import HTTPException, Response
from pydantic import BaseModel, validators
from enum import Enum
from datetime import datetime
from typing import Optional, List
from pymysql import Connection, cursors
import pymysql
from app.core import config
import logging, json
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
    user: Optional[str]
    judul: Optional[str]
    slug: Optional[str]
    tag: Optional[str]
    keyword: Optional[str]
    status: Optional[BeritaStatus] = BeritaStatus.publish
    kategori: Optional[int]
    limit: int = 100


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
                args['status'] = str(args['status'].value)
                args['kategori'] = ','.join([str(x) for x in args['kategori']])
                cur.execute(query=insert_query, args=args)
        except Exception as e:
            logging.error(e)
            conn.rollback()
            raise HTTPException(
                status_code=400,
                detail='insert error, due to malformed request or wrong data')
        conn.commit()


async def get_berita(params: GetBerita):
    query = '''SELECT judul,user,isi,slug,tag,keyword,kategori FROM berita '''

    where = ''
    limit = ''
    if params.user:
        where += """user=%(user)s """

    if params.status is not None:
        if where:
            where += """AND """
        where += """status=%(status)s """

    if params.judul:
        if where:
            where += """AND """
        where += """judul LIKE %(judul)s """

    if params.slug:
        if where:
            where += """AND """
        where += """slug LIKE  %(slug)s """

    if params.tag:
        if where:
            where += """AND """
        where += """tag LIKE  %(tag)s """

    if params.keyword:
        if where:
            where += """AND """
        where += """keyword LIKE  %(keyword)s """

    if params.kategori:
        if where:
            where += """AND """
        where += """kategori LIKE  %(kategori)s """

    if params.limit:
        limit += """LIMIT %(limit)s """

    where = "WHERE " + where
    query += where
    query += limit

    conn = Connection(user=config.DB_USER,
                      password=config.DB_PASS,
                      database=config.DB_NAME,
                      host=config.DB_HOST,
                      cursorclass=cursors.DictCursor)

    res = None

    with conn:
        args = params.dict()
        args['status'] = str(args['status'].value)
        try:
            with conn.cursor() as cur:
                cur.execute(query=cur.mogrify(query=query, args=args))
                res = cur.fetchall()

        except Exception as e:
            logging.error(e)
            raise HTTPException(
                status_code=400,
                detail='insert error, due to malformed request or wrong data')

    return res

from typing import Optional
from fastapi import APIRouter, Query
from app.core.presenter import berita as berita_p
from app.core.model import berita as berita_m

router = APIRouter()


# @router.get("/berita/{offset}/{limit}")
# async def get_berita():
#     return {}


@router.post("/berita")
async def post_berita(params: berita_m.SetBerita):
    await berita_p.set_berita(params)

from typing import Optional, List
from fastapi import APIRouter
from app.core.presenter import berita as berita_p
from app.core.model import berita as berita_m

router = APIRouter()


@router.get("/berita")
async def get_berita(user: Optional[str] = None,
                     judul: Optional[str] = None,
                     slug: Optional[str] = None,
                     tag: Optional[str] = None,
                     keyword: Optional[str] = None,
                     status: Optional[int] = 1,
                     kategori: Optional[str] = None,
                     limit: Optional[int] = 100):

    params = berita_m.GetBerita(user=user,
                                judul=judul,
                                slug=slug,
                                tag=tag,
                                keyword=keyword,
                                status=status,
                                kategori=kategori,
                                limit=limit)

    def __normalize(params: berita_m.GetBerita) -> berita_m.GetBerita:
        params.user = f'%{params.user}%' if params.user else ''
        params.judul = f'%{params.judul}%' if params.judul else ''
        params.slug = f'%{params.slug}%' if params.slug else ''
        params.tag = f'%{params.tag}%' if params.tag else ''
        params.keyword = f'%{params.keyword}%' if params.keyword else ''
        params.kategori = f'%{params.kategori}%' if params.kategori else ''
        return params

    return await berita_p.get_berita(__normalize(params))


@router.post("/berita")
async def post_berita(params: berita_m.SetBerita):
    await berita_p.set_berita(params)

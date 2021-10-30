from fastapi import APIRouter
from app.core.presenter import berita as berita_p
from app.core.model import berita as berita_m

router = APIRouter()


@router.post("/get_berita")
async def get_berita(params: berita_m.GetBerita):
    return await berita_p.get_berita(params)


@router.post("/set_berita")
async def post_berita(params: berita_m.SetBerita):
    await berita_p.set_berita(params)

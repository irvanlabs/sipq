from app.core.model import berita as berita_m


async def set_berita(params: berita_m.SetBerita):
    await berita_m.set_berita(params)


async def get_berita(params: berita_m.GetBerita):
    return await berita_m.get_berita(params)

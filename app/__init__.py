from fastapi import FastAPI
from app.core import config
from app.api.v1 import example


def init_application() -> FastAPI:
    application = FastAPI(title=config.APP_NAME,
                          version=config.VERSION,
                          debug=config.DEBUG)

    application.include_router(example.router, prefix='/api/v1')
    return application


app = init_application()

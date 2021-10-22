from fastapi import FastAPI
from app.core import config
from app.api.v1 import example, register, upgrade_level


def init_application() -> FastAPI:
    application = FastAPI(title=config.APP_NAME,
                          version=config.VERSION,
                          debug=config.DEBUG)

    # application.include_router(example.router, prefix='/api/v1')
    application.include_router(register.router, prefix=config.API_PREFIX)
    application.include_router(upgrade_level.router, prefix=config.API_PREFIX)
    return application


app = init_application()

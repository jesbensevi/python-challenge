import os

from app.config import db
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel


class Settings(BaseModel):
    authjwt_secret_key: str = os.environ.get("SECRET_KEY")
    authjwt_token_location: set = {"cookies"}
    authjwt_cookie_csrf_protect: bool = False


@AuthJWT.load_config
def get_config():
    return Settings()


def init_app():
    db.init()

    app = FastAPI(
        title="API App",
        version="1"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    # add authjwt_token_location

    @app.on_event("shutdown")
    async def shutdown():
        await db.close()

    from app.controller import login

    app.include_router(login.router)
    # app.include_router(users.router)

    return app


app = init_app()

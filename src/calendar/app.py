from sqlmodel import SQLModel
from fastapi import FastAPI
from src.calendar.extensions.db import engine
from src.calendar.entity import * # noqa
from src.calendar.views.users import app as users_app


def get_app():
    SQLModel.metadata.create_all(engine)
    app = FastAPI()
    app.include_router(users_app)
    return app

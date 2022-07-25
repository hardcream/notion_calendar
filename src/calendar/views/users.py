from fastapi import APIRouter, Body
from src.calendar.model import UserCreate

app = APIRouter(prefix="/users")


@app.get("/")
def users_list():
    return {"hello": "world"}


@app.get("/{user_id:str}")
def users_retrieve(user_id):
    pass


@app.post("/")
def users_create(data: UserCreate = Body(...)):
    name = data.username
    password = data.password


@app.delete("/{user_id:str}")
def users_destroy(user_id):
    pass


@app.patch("/{user_id:str}")
def users_update(user_id):
    pass


__all__ = ["app"]

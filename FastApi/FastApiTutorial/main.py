from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    name: str
    description: str | None = None
    surname: str
    tax: float | None = None


app = FastAPI()


@app.get("/")
async def get():
    return {"message": "hola mundo"}


@app.post("/user/")
async def create_item(user: User):
    return user

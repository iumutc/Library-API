from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter


class Book(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    publisher: str

class Journal(BaseModel):
    id: int
    name: str
    editor: str
    press: str

app = FastAPI(title="Learning API",description="Trying",version="0.0.1")
app.include_router(CRUDRouter(schema=Book))
app.include_router(CRUDRouter(schema=Journal))

from fastapi import FastAPI 
from . import models
from .database import engine
from .routers import blogs , users

# creating the app 
app = FastAPI()

# creating database schemas and tables.
models.Base.metadata.create_all(engine)

app.include_router(blogs.router)
app.include_router(users.router)
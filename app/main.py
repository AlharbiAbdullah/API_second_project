from fastapi import FastAPI 
from blogs import models
from blogs.database import engine
from blogs.routers import blogs , users, login

# creating the app 
app = FastAPI()

# creating database schemas and tables.
models.Base.metadata.create_all(engine)

app.include_router(login.router)
app.include_router(blogs.router)
app.include_router(users.router)

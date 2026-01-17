from contextlib import asynccontextmanager
from fastapi import FastAPI
from options.router import router as options_router
from choices.router import router as choices_router
from db import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables..")
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(options_router)
app.include_router(choices_router)

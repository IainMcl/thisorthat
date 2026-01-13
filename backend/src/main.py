from fastapi import FastAPI
from options.router import router as options_router
from choices.router import router as choices_router

app = FastAPI()
app.include_router(options_router)
app.include_router(choices_router)

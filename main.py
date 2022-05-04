from fastapi import FastAPI
from src.api import mainApiRouter

app = FastAPI()
app.include_router(mainApiRouter.router)

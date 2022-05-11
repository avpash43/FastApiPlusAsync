from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.api import main_api_router
from src.repository.database import database

app = FastAPI()
app.include_router(main_api_router.router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": f"Oops! File not chosen... Error message: {exc}"},
    )

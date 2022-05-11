from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.api import MainApiRouter

app = FastAPI()
app.include_router(MainApiRouter.router)


@app.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": f"Oops! File not chosen... Error message: {exc}"},
    )

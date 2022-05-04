from fastapi import APIRouter

router = APIRouter(
    prefix="/url",
    tags=["url"],
    responses={404: {"description": "Not found"}},
)


@router.get("/make_request_by_list")
async def add_url_list():
    # ToDo: handle ingest url list
    return {"Hello": "World"}

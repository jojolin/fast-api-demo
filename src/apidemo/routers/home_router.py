from fastapi import APIRouter
from starlette.responses import HTMLResponse

router = APIRouter()


@router.get("/")
async def home():
    return HTMLResponse(
        content='<ul><li><a href="http://localhost:8000/docs">docs</a></li>'
                '<li><a href="http://localhost:8000/redoc">redoc</a></li></ul')

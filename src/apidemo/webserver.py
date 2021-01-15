import uvicorn
from fastapi import Depends, FastAPI

from . import config
from .routers import items_router, users_router, bgtask_router, depend_router, async_router, serv_rounter, home_router

app = FastAPI()
app.include_router(
    home_router.router,
    tags=["home"],
    responses={418: {"description": "I'm a teapot"}},
)
app.include_router(users_router.router)
app.include_router(items_router.router)
app.include_router(bgtask_router.router)
app.include_router(async_router.router)
app.include_router(serv_rounter.router)
app.include_router(depend_router.router)


@app.get("/info")
async def info(settings: config.Settings = Depends(config.get_settings)):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }


if __name__ == '__main__':
    uvicorn.run(app, port=8000)

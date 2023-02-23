from aiohttp import web
from models import Session

@web.middleware
async def session_middleware(
        request: web.Request,
        handler,                       # хэндлер - это views (в него закидывается views)
):
    async with Session() as session:
        request['session'] = session   #передаем сессию через объект request
        return await handler(request)
from aiohttp import web
from service.routes import router


def create_app():
    app = web.Application()
    app.add_routes(router)
    return app

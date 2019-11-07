from aiohttp import web
from .routes import router


def create_app():
    app = web.Application()
    app.add_routes(router)
    return app

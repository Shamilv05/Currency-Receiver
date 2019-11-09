from service.app import create_app
from service.routes import currency

import asyncio
from aiohttp import web

import nest_asyncio

nest_asyncio.apply()


async def main():
    asyncio.create_task(currency("https://api.ratesapi.io/api/latest"))
    web.run_app(create_app(), port=8090)


asyncio.run(main())

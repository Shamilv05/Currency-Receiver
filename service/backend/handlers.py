from aiohttp import web, ClientSession
from backend.logger import log
import asyncio
import json

rate = {"data": "No Data"}


async def currency(url: str):
    global rate
    while True:
        async with ClientSession() as session:
            async with session.get(url) as resp:
                rate = await resp.read()
                rate = json.loads(rate)
        await asyncio.sleep(3)


async def currency_get(request):
    log.info(request)
    return web.json_response(rate)

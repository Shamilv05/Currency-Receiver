import aiohttp
import asyncio
import json

rate = {"data": "No Data"}


async def currency(url: str):
    global rate
    while True:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                rate = await resp.read()
                rate = json.loads(rate)
        await asyncio.sleep(3)

router = aiohttp.web.RouteTableDef()


@router.get('/')
async def currency_get(request):
    return aiohttp.web.json_response(rate)

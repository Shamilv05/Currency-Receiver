import aiohttp
import asyncio

rate = None


async def currency(url: str):
    global rate
    while True:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                rate = await resp.read()
        await asyncio.sleep(3)

router = aiohttp.web.RouteTableDef()


@router.get('/')
async def currency_get(request):
    return aiohttp.web.Response(text=f"data: {rate}")

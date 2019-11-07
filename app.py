import asyncio
import aiohttp


async def currency(url: str):
    while True:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                response = await resp.read()
                print(response)
                await asyncio.sleep(3)


loop = asyncio.get_event_loop()
loop.run_until_complete(currency('https://api.ratesapi.io/api/latest'))

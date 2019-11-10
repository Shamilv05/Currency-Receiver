import aiohttp.web
from aiomisc import entrypoint
from aiomisc.service.aiohttp import AIOHTTPService
from backend.handlers import currency_get, currency


class CurrencyReciever(AIOHTTPService):
    async def create_application(self):
        app = aiohttp.web.Application()

        app.add_routes([
            aiohttp.web.get('/', currency_get)
        ])

        return app


def main():
    service = CurrencyReciever(address='0.0.0.0', port=8090)

    with entrypoint(service) as loop:
        loop.create_task(currency('https://api.ratesapi.io/api/latest'))
        loop.run_forever()


if __name__ == "__main__":
    main()

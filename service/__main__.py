import aiohttp
from aiomisc import entrypoint
from aiomisc.service.aiohttp import AIOHTTPService
from backend.handlers import currency_get, currency
from backend.logger import log


class CurrencyReciever(AIOHTTPService):
    async def create_application(self):
        app = aiohttp.web.Application()

        app.add_routes([
            aiohttp.web.get('/', currency_get)
        ])
        log.info(f'Service has started')

        return app


def main():
    service = CurrencyReciever(address='0.0.0.0', port=80)

    with entrypoint(service) as loop:
        log.info('Loop created')
        loop.create_task(currency('https://api.ratesapi.io/api/latest'))
        loop.run_forever()


if __name__ == "__main__":
    main()

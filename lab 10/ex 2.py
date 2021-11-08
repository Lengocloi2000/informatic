import time
import asyncio
import aiohttp
from collections import namedtuple
from concurrent.futures import FIRST_COMPLETED

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query'),
)

async def fetch_ip(service):
    start = time.time()
    try:
        async with aiohttp.request('GET', service.url) as response:
            json_response = await response.json()
            ip = json_response[service.ip_attr]
            print('{} finished with result: {}, took: {:.2f} seconds'.format(
                service.name, ip, time.time() - start))
            return ip
    except:
        return '{} is unresponsive'.format(service.name)

async def asynchronous():
    futures = [fetch_ip(service) for service in SERVICES]
    done, pending = await asyncio.wait(futures, return_when=FIRST_COMPLETED)

    for future in pending:
        future.cancel()

    print(done.pop().result())

ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
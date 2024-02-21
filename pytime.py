import asyncio
import aiohttp
from colorama import Fore
from datetime import datetime

interval = 1 # add interval

async def checker(url):
    async with aiohttp.ClientSession() as session:
        try:
            start = datetime.now()
            async with session.get(url, timeout=10) as response:
                end = datetime.now()
                response_time = (end - start).total_seconds()
                sc = response.status
                if sc == 200:
                    print(f"\n\n{Fore.GREEN}{url} is UP! [ Response: {response_time}s ]")
                else:
                    print(f"\n\n{Fore.RED}{url} is DOWN! [ Status Code: {sc} ]")
        except (aiohttp.ClientConnectorError, aiohttp.ClientError, asyncio.TimeoutError) as e:
            print(f"{Fore.MAGENTA}Failed to establish connection with {url}! Error: {e}")

async def main():
    urls = ["https://bleed.bot","https://guns.lol", "https://google.com", "https://youtube.com"] # add/remove your url
    while True:
        tasks = [checker(url) for url in urls]
        await asyncio.gather(*tasks)
        await asyncio.sleep(interval)

if __name__ == "__main__":
    asyncio.run(main())

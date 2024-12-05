import aiohttp,asyncio,os


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://httpbin.org/get") as res:
            print(res.status)
            print(await res.read())
            print(await res.text(encoding="utf-8"))
            print(await res.json())

os.system("cls")
asyncio.run(main())
import aiohttp,asyncio,os


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://httpbin.org/get",params={"key":"value",}) as res:
            print(res.status)
            print(await res.text(encoding="utf-8"))
            print(res.url)

os.system("cls")
asyncio.run(main())
import aiohttp,asyncio,os


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post("http://httpbin.org/post",data="传递数据") as res:
            print(res.status)
            
            print(await res.text())
            print(res.request_info)
            

os.system("cls")
asyncio.run(main())




import asyncio,aiofiles


async def main():
    async with aiofiles.open(".//1-11协程//aiofile异步读写文件//文本.txt",'r',encoding="utf-8") as fp:
        return await fp.read() #为什么使用await才能读取到数据，因为读取数据需要时间，所以要挂起，也可到read的声明处发现其定义为async
print(asyncio.run(main()))
import asyncio,aiofiles


async def main():
    async with aiofiles.open(".//1-11协程//aiofile异步读写文件//文本.txt",'w',encoding="utf-8") as fp:
        await fp.write("hello dahshabi") #为什么使用await才能写入数据，因为写数据需要时间，所以要挂起，也可到write的声明处发现其定义为async

asyncio.run(main())
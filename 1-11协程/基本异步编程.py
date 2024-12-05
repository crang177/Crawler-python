import asyncio

async def run():
    
    print("hello")
    await asyncio.sleep(2)
    print("good")
    return 2

def callback(f):
    print("返回值====",f.result())
if __name__=="__main__":
    cor=run()
    #asyncio.run(cor)

    task=asyncio.ensure_future(cor)

    task.add_done_callback(callback)

    loop=asyncio.get_event_loop()
    loop.run_until_complete(task)

import asyncio,aiohttp
from proxy_redis import ProxyRedis



async def test_ip(sem,ip,redis):
    try:
        async with sem:
            async with aiohttp.ClientSession() as session:
                async with session.get("http://httpbin.org/ip",proxy="http://"+ip,timeout=10) as res:
                    text = await res.text()
                    if text :
                        redis.zset_add(ip)
                    else:
                        redis.zset_zincrby(ip)
                        print(ip,"权重降低")
    except:
        redis.zset_zincrby(ip)
        print(ip,"权重降低")
  







async def main():
    redis=ProxyRedis()
    all_ip=redis.get_all_ip()

    sem=asyncio.Semaphore(100)
    task_list=[asyncio.create_task(test_ip(sem,i,redis)) for i in all_ip]
    await asyncio.wait(task_list)

def run():
    while True:
        try :
            asyncio.run(main())
        except:
            pass
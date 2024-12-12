"""
    获取ip
"""

import requests
import re
from proxy_redis import ProxyRedis


def get_ip():
    url="https://www.kuaidaili.com/free/inha/"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    }
    res=requests.get(url,headers=headers) 
    res.encoding=res.apparent_encoding
    print(res.status_code)
    # with open( "1-18代理池/kuaidaili.html","w",encoding="utf-8") as fp:
    #     fp.write(res.text)


    regexes=re.compile(r'ip": "(.*?)", "la.*?port": "(.*?)",')

    # with open( "1-18代理池/kuaidaili.html","r",encoding="utf-8") as fp:
    #     data=fp.read()

    data=res.text

    ls=regexes.findall(data)
    redis=ProxyRedis()
    for i in ls:
        ip=i[0]+":"+i[1]
        
        #将数据存入redis中
        redis.zset_add(ip)
        print(ip,"已存入redis中")

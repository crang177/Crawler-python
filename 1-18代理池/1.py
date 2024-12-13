import requests
import re
from proxy_redis import ProxyRedis
from lxml import etree




url="http://ip.ihuan.me/"

# proxy={
#     "http":"61.160.202.71:80"
# }

# res=requests.get(url="http://httpbin.org/ip",proxies=proxy) 
# res.encoding=res.apparent_encoding
# print(res.text)


headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "Referer":"http://ip.ihuan.me/",
    "Cookie":'cc40d46e2bfd29a628defb7cf26ab17e=75a0336aceb2bc9c2cea69d329501619; 9144eeb120922f188b899bf0bf597e02=b962ddc8d4d8397f9a150e7d1f07daed'
}

res=requests.get(url,headers=headers) 
res.encoding=res.apparent_encoding

print(res.status_code)
with open( "1-18代理池/xiaohuan.html","w",encoding="utf-8") as fp:
    fp.write(res.text)




selector=etree.HTML(res.text)
ip_ls=selector.xpath("//tbody//tr/td[1]/a/text()")

port_ls=selector.xpath("//tbody/tr/td[2]/text()")
print(port_ls)

for i in range(len(port_ls)):

    ip= ip_ls[i]+":"+port_ls[i]
    print(ip)
    
    
 

     

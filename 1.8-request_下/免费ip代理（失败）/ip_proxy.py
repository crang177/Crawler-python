import requests,os


os.system("cls")
proxy = {
    'http': '218.75.102.198:8000'
}

result = requests.get("http://httpbin.org/ip",proxies=proxy,timeout=3)
print(result.text)
result = requests.get("http://www.baidu.com",proxies=proxy,timeout=3)
print(result.status_code)

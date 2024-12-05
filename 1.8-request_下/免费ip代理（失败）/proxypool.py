import requests
import re,os,time


l=[]
regexes=re.compile(r'{"ip": "(.*?)", "last_check_time": ".*?", "port": "(.*?)",')

os.system("cls")
url="https://www.kuaidaili.com/free/inha/"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "Cookie":"channelid=0; sid=1732632145505150; _ss_s_uid=3ef7200f865bd0c21b8cf41559376116",
}
res=requests.get(url,headers=headers)
res.encoding=res.apparent_encoding
ls=regexes.findall(res.text)
for i in ls :
    l.append(i[0]+":"+i[1])
    

url="https://www.kuaidaili.com/free/inha/2"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "Cookie":"channelid=0; sid=1732632145505150; _ss_s_uid=3ef7200f865bd0c21b8cf41559376116",
}
res=requests.get(url,headers=headers)
res.encoding=res.apparent_encoding
ls=regexes.findall(res.text)
for i in ls :
    l.append(i[0]+":"+i[1])



ke=[]
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
}
for i in l:
    print(i)
    proxy = {
        'http': i
        }
    try:
        result = requests.get("http://www.baidu.com",headers=headers,proxies=proxy,timeout=0.5)
        print(result.status_code)
        ke.append(i)
    except:
        pass

print(ke)




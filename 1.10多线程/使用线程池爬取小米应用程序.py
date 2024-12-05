import requests,time,os,random
from lxml import etree
from concurrent.futures import ThreadPoolExecutor


def get(n):
    print(f"开始爬取第{n}页")
    url="https://app.mi.com/allCloudGames?page={}".format(n)
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
        "Referer":"https://app.mi.com/allCloudGame",
    }
    res=requests.get(url=url,headers=headers)
    res.encoding=res.apparent_encoding
    selector=etree.HTML(res.text)
    ls=selector.xpath('//ul[@class="applist index-cloud-list"]/li')
    for i in ls:
        name=i.xpath("./a/img/@alt")[0]
        web=i.xpath("./h5/a/@href")[0]
        print(f"游戏名字：{name}  网址：{web}")
    time.sleep(3)
    #print(f"第{n}页爬取完毕 \n\n")



if __name__=="__main__":
    os.system("cls")
    pool=ThreadPoolExecutor(2)

    arg=[1,2,3]
    pool.map(get,arg)
    pool.shutdown()

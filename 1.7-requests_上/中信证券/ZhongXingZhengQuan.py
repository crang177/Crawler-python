
import requests
from lxml import etree
import os
import csv

def spider(url):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",

    }
    res=requests.get(url=url,headers=headers)
    res.encoding=res.apparent_encoding

    selector=etree.HTML(res.text)
    ls=selector.xpath('//ul[@class="list-con"]/li')
    return  ls
 


def write_message(ls):
    global n
    n+=1
    with open("1.8-requests\中信证券\中信证券销售金融产品信息公示.csv","a",newline='') as fp:
        w=csv.writer(fp)       
        for i in ls:
            name,company,level,money=i.xpath("./span/text()")[0:4]
            w.writerow([name,'','','','','','','','','',company,'','',level,'',money])
    print(f"当前的页数: {n}")

def main():
    ls=spider("http://www.cs.ecitic.com/newsite/cpzx/jrcpxxgs/zgcp/index.html")
    
    with open("1.8-requests\中信证券\中信证券销售金融产品信息公示.csv","a",newline='') as fp:
        w=csv.writer(fp)
        w.writerow(["产品名称",'','','','','','','','','','管理人','','','风险评级','','认购金额起点'])
    while True:
        write_message(ls)
        next=f"http://www.cs.ecitic.com/newsite/cpzx/jrcpxxgs/zgcp/index_{n}.html"
        if n==103:
            break
        else:
            ls=spider(next)

n=0
if __name__=="__main__":
    os.system("cls")
    main()
import requests,os,csv,json
from lxml import etree

url="https://cang.cngold.org/c/2024-11-19/c9593865.html"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
}
os.system("cls")
res=requests.get(url=url,headers=headers)
res.encoding=res.apparent_encoding
# with open ("1.8-requests\金投网\现在银元价格.html","w",encoding="utf-8") as fp:
#     fp.write(res.text)

selector=etree.HTML(res.text)
ls=selector.xpath("//tbody/tr")

with open("1.8-requests\金投网\现在银元价格.csv","w",newline='') as fp:
    w=csv.writer(fp)
    w.writerow(["名称",'','品相','','价格'])
    w.writerow(["",'','','',''])
    for i in ls[1:-1]:
        name=i.xpath("./td[1]/text()")[0]
        type=i.xpath("./td[2]/text()")[0]
        price=i.xpath("./td[3]/text()")[0]
        w.writerow([name,'',type,'',price])

with open("1.8-requests\金投网\现在银元价格.csv","r",) as fp:
    reader=csv.reader(fp)
    for i in reader:
        print(i)

import requests
from lxml import etree
import os
import csv



os.system("cls")
url="https://www.shicimingju.com/bookmark/sidamingzhu.html"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",

}

res=requests.get(url=url,headers=headers)
res.encoding=res.apparent_encoding
selector=etree.HTML(res.text)#创建选择器对象
ls=selector.xpath('//div[@class="list clear theme2 theme3"]/a')



with open ("1.8-requests\四大名著\四大名著.csv","w",newline='') as fp:
    w=csv.writer(fp)
    w.writerow(["四大名著",'','网站'])
    for i in ls:
        web='https://www.shicimingju.com/'+i.xpath("./@href")[0]
        name=i.xpath('./p/text()')[0]
        w.writerow([name,'',web])


with open ("1.8-requests\四大名著\四大名著.csv","r",encoding="gbk") as fp:
    reader=csv.reader(fp)
    for i in reader:
        print(i)
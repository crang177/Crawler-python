
import requests
from lxml import etree
import os
import csv


os.system("cls")
url="https://www.shicimingju.com/book/sanguoyanyi.html"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",

}

res=requests.get(url=url,headers=headers)
res.encoding=res.apparent_encoding
selector=etree.HTML(res.text)#创建选择器对象
ls=selector.xpath('//div[@class="list"]/a')
with open ("1.8-requests\三国演义\三国演义章节.csv","w",newline='') as fp:
     #写入csv文件时，要将newline=''，否则会出现多余的几行

    w=csv.writer(fp) #将csv文件对象创建改变为写入的对象，使用的writer（）函数，还有一种Dicwriter类
    w.writerow(["章节",'','','','',"网站"])#按一行一行的写入，因为使用的是writer（）函数，所以此处参数为一个列表，表示内容，列表的每一个元素代表一个单元格
    for i in ls :
        name=i.xpath("./text()")[0]
        web="https://www.shicimingju.com"+i.xpath("./@href")[0]
        w.writerow([name,'','','','',web])
    
    
with open ("1.8-requests\三国演义\三国演义章节.csv","r",newline='',encoding="gbk") as fp:#读取csv文件
    reader=csv.reader(fp)#使用csv内置的reader（）函数，传入文件对象，将会返回一个reader对象（可迭代对象），该对象的每一个元素为一个列表，每一个列表都代表了csv文件中的一行
    for r in reader:
        print(r)

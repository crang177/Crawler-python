import requests
from lxml import etree
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Referer":"https://www.xigushi.com/",
}
res=requests.get("https://www.xigushi.com/mrgs/15060.html",headers=headers)
res.encoding=res.apparent_encoding
text= res.text

selector=etree.HTML(text)
ls=selector.xpath("//div[@class='by']")
for i in selector:
    title=i.xpath("./h1/text()")
    print(title)
#                 author=regexes.findall(i.xpath("./div/text()")[0])[0]
#                 body=i.xpath("./p/text()")[0]
#                 task_ls.append((title,author,body))

import requests

#爬取17k小说网

url="http://passport.17k.com/ck/user/login"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "Referer":"http://passport.17k.com/login/",
}
data={
    "loginName": "18008567665",
    "password": "a123456",
}

session=requests.Session()
a=requests.post(url=url,headers=headers,data=data)
print(a.text)


headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "Referer":"https://user.17k.com/www/bookshelf/index.html",
}
res=session.get("https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919",headers=headers)
res.encoding=res.apparent_encoding
print(res.text)




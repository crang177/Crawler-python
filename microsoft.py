import requests,os,hashlib,time

print(int(time.time()*100))






url="https://cn.bing.com/ttranslatev3?isVertical=1&&"+f"IG={}"+"&IID=translator.5026"
url="https://cn.bing.com/translator"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Referer":"https://cn.bing.com/translator",
    #"Cookie":''
}



data={
    "fromLang": "zh-Hans",
    "to": "en",
    "text": "你好",
    "tryFetchingGenderDebiasedTranslations": "true",

    "token": "",
    "key": f"{int(time.time()*100)}"
}
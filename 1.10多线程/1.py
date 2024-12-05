import requests,os,time,random
from lxml import etree
from concurrent.futures import ThreadPoolExecutor









url="http://pic.netbian.com/4kfengjing/"

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",

    'Referer':'https://pic.netbian.com/',
    "Cookie":'cf_clearance=HjbPsloIQsUzOIFOtzZWniOnTpIPfWycYrcDuAVGSD8-1733120220-1.2.1.1-boatFPdffdSOvt24CBrGggefurQtf.RtSr1UImUMT19RMbkxoGtfKHPAXvBE7vtpztApUP54.rfx_GgmGX1mPScRo0hx0iP9f.s4yimutmVU_q5.jYql.TmDqHqVyW7KxmwGi5Hu.UKDWWdLSm4aeOI_tqrqB9rw9il1U79xkpTXgJdJvTdJpP1O5HCsZMshTZsFLGJIGeTlDVBqlgoJM4gYUx7X5pDuQGn3SxyQqDKs8h..38.l5CoJOd4OkEraLYnDS829eKeR8.va9diKfW3U0UBmYjSvsWxqpwDSxwhQSP4FWEHR_BCUJgWNpM3iRXildpN6RdEmQglzi4jsNtcgZgm50nj4jOw1N_l3jT8pCwHFK2k.EKsJ.G1KxceJhKxWH_n.ANJQQwZ68ih2n176yKiJ8NUCN03yyCADqVq_NNwDRg_oSqeTI9RQe1YuLoly9ijWBQ14kNeuaVVBfA; zkhanecookieclassrecord=%2C53%2C; PHPSESSID=m9g67kduk978e9db12945go9k7; zkhanmlusername=Cran; zkhanmluserid=7341918; zkhanmlgroupid=1; zkhanmlrnd=2O5kNfBSfNGrUpcKMZ0q; zkhanmlauth=16ffdca362b5f6bb8ee4a9f6780cb0d1'
}


res=requests.get(url,headers=headers)
res.encoding=res.apparent_encoding
print(res)

# selector=etree.HTML(res.text)

# ls=selector.xpath('//ul[@class="clearfix"]/li')
# print(ls)
# for i in ls :

#     pic_url="https://pic.netbian.com"+i.xpath("./a/@href")
#     name=i.xpath("./b/text()")

#     res=requests.get(pic_url,headers=headers)
#     res.encoding=res.apparent_encoding

#     selector=etree.HTML(res.text)
#     download_url="https://pic.netbian.com"+selector.xpath('//a[@id="img"]/img/@src')

#     download_res=requests.get(download_url,headers=headers)
#     with open(f"./1.10多线程/彼岸图/{name}.jpg") as fp:
#         fp.write(download_res.content)
    

# time.sleep(random.randint(2,4))







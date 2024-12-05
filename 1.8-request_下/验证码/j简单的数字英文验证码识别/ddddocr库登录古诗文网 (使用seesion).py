import ddddocr
import requests,os
from lxml import etree



def identify_code():#先找到验证码的url，然后保存url，使用session的原因：对于图片的url来说，每访问一次就会刷新一次，验证码就会改变，所以要用session来维持当前的会话，此时若发送登录的请求就是使用的是当前的验证码
    #然后使用ddddocr库来识别验证码

    os.system("cls")
    pic_url="https://www.gushiwen.cn/RandCode.ashx"
    
    pic_res=session.get(pic_url)
    with open("1.8-request_下\验证码\j简单的数字英文验证码识别\yzm_poetry.jpg","wb") as fp:
        fp.write(pic_res.content)


    ocr=ddddocr.DdddOcr(show_ad=False)#show_ad=False省略掉行业标语，实例化
    with open("1.8-request_下\验证码\j简单的数字英文验证码识别\yzm_poetry.jpg","rb") as fp:
        pic_bytes=fp.read()#读取图片
    pic_yzm=ocr.classification(pic_bytes).upper()#识别验证码
    return pic_yzm




def login(pic_yzm):#登录网站：全部用的都是session，即一直维持着会话，登录前和登陆后的cookie不一样，session的作用是自动使用上一次的cookie，会自己更新
    url='https://www.gushiwen.cn/user/login.aspx?'
    headers={
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        "Referer":'https://www.gushiwen.cn/user/login.aspx?'
    }
    params={
        "from": "http://www.gushiwen.cn/user/collect.aspx"
    }

    data={
        "__VIEWSTATE":'6q36H7Ym3+NSJXnBxUg3VPnL1m1TzyGgvuv0XoWsgAoJY+WQU+zm6F/I0fZyrBJinka5Z2wJ25i2vAEE+NrVRi4YgjietlQyWSFUYdgT/ck4+TPJCIyZJw206Y8xCUVd5BnYkuC+GQvbF70vqi06hAjZx7g=',
        "__VIEWSTATEGENERATOR": 'C93BE1AE',
        "from": "http://www.gushiwen.cn/user/collect.aspx",
        "email": "18008567665",
        "pwd": "a12345",
        "code": pic_yzm,#验证码
        "denglu": "登录",
    }
    session.post(url=url,headers=headers,params=params,data=data)#发送登录的请求







def main():
    pic_yzm=identify_code()
    login(pic_yzm)

    a=session.get('https://www.gushiwen.cn/shiwens/default.aspx?astr=%e6%9d%8e%e7%99%bd')
    a.encoding=a.apparent_encoding
    selector=etree.HTML(a.text)
    ls=selector.xpath('//div[@class="contson"]')
    for i in ls:
        p=i.xpath("./p/text()")
        if p!=[]:
            for j in p:
                print(j)
            print()


if __name__=="__main__":
    session=requests.Session()
    main()


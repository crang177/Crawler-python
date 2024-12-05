import ddddocr
import requests

# pic_url="https://www.gushiwen.cn/RandCode.ashx"
# pic_res=requests.get(pic_url)
# with open("1.8-request_下\验证码\j简单的数字英文验证码识别\yzm.jpg","wb") as fp:
#     fp.write(pic_res.content)

ocr=ddddocr.DdddOcr(show_ad=False)#show_ad=False省略掉行业标语，实例化
with open("1.8-request_下\验证码\j简单的数字英文验证码识别\yzm.jpg","rb") as fp:
    pic_bytes=fp.read()#读取图片
pic_yzm=ocr.classification(pic_bytes).upper()#识别验证码
print(pic_yzm)
"""
    获取ip,利用flask框架，将满足的ip显示在网页 http://127.0.0.1:5000/ 上
"""

from flask import Flask
from proxy_redis import ProxyRedis




#http://127.0.0.1:5000/


app = Flask(__name__)
@app.route('/')
def index():
    redis=ProxyRedis()

    #   从redis数据库中得到有效的ip（经过测试过的ip）
    #   如果得到了ip就将ip返回，返回到网站的信息中
    ip=redis.get_ip()
    if ip :
        return ip
    
    #   如果ip不存在就返回 “来了”
    return "来了"


#启动flask框架
def run():
    app.run()













 


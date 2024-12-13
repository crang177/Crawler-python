"""
    获取ip
"""

from flask import Flask
from proxy_redis import ProxyRedis

app = Flask(__name__)


#http://127.0.0.1:5000/
@app.route('/')


def index():
    redis=ProxyRedis()
    ip=redis.get_ip()
    if ip :
        return ip
    return "来了"


#启动flask框架
def run():
    app.run()













 


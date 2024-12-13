import redis,random

from settings import *

class ProxyRedis:
    def __init__(self):

        self.r = redis.Redis(host=HOST,port=PORT,password=PASSWORD,db=DB,decode_responses=True)

    #添加ip
    def zset_add(self,ip):
        self.r.zadd(ZSET_NAME,{ip:SCORE})

    # 处理权重
    def zset_zincrby(self,ip):
        #查看当前ip的权重
        score=self.r.zscore(ZSET_NAME,ip)

        if score>MIN_SCORE:
            
            self.r.zincrby(ZSET_NAME,-1,ip)

        else:
            print(f"{ip} 不可用，已删除")
            self.r.zrem(ZSET_NAME,ip)

    def get_all_ip(self):#获取所有ip
        return self.r.zrange(ZSET_NAME,0,-1)
        
    
    #获取可用的ip
    def get_ip(self) :
        ip_ls=self.r.zrangebyscore(ZSET_NAME,SCORE,SCORE,0,-1)
        if ip_ls:
            return random.choice(ip_ls)
        ip_ls=self.r.zrangebyscore(ZSET_NAME,MIN_SCORE,SCORE,0,-1)
        if ip_ls:
            return random.choice(ip_ls)
        else:
            print("当前无可用的ip")

        



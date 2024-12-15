# 存储，修改ip，获得数据库中的ip
"""
    构造一个类来实现相应功能
    redis有序集合部分命令:
        zadd  添加
        zscore  获取成员的权重
        zincrby  增加减少权重
        zrange  获取范围区间的ip
        zrangebyscore   获取权重范围区间的ip
        zrem  删除
"""

import redis,random
from settings import *

class ProxyRedis:

    def __init__(self):
        #   连接redis数据库
        #   host主  机名
        #   port    端口
        #   passsword   密码
        #   db  要连接的redis库的哪个库（0~15）
        #   decode_responses    自动解码
        self.r = redis.Redis(host=HOST,port=PORT,password=PASSWORD,db=DB,decode_responses=True)

    #添加ip到数据库中
    def zset_add(self,ip):
        #   第一个参数为  有序集合的名字
        #   {ip:SCORE} 是将ip的权重设置为 SCORE
        self.r.zadd(ZSET_NAME,{ip:SCORE})

    # 处理权重 : 当ip验证失败后，如果ip的权重大于70（MIN_SCORE自己设置的最小权重），则将其权重减一；如果其现在的权重已经小于MIN_SCORE，则舍弃，删除这个ip
    def zset_zincrby(self,ip):
        #查看当前ip的权重
        score=self.r.zscore(ZSET_NAME,ip)

        if score>MIN_SCORE:
            #   将有序集合ZSET_NAME中的一个ip的权重 -1
            self.r.zincrby(ZSET_NAME,-1,ip)

        else:
            print(f"{ip} 不可用，已删除")
            #   不可用就删除ip
            self.r.zrem(ZSET_NAME,ip)

    def get_all_ip(self):#获取所有ip
        #zrange  获取范围区间的ip，0和-1就是指的是全部
        return self.r.zrange(ZSET_NAME,0,-1)
        
    
    #获取可用的ip
    def get_ip(self) :
        #zrangebyscore   获取权重范围区间的ip
        #第一次的筛选，直接得到最大值，得到一个列表
        ip_ls=self.r.zrangebyscore(ZSET_NAME,SCORE,SCORE,0,-1)
        if ip_ls:
            return random.choice(ip_ls)#随机返回一个有效ip
        
        # 第二次筛选
        ip_ls=self.r.zrangebyscore(ZSET_NAME,MIN_SCORE,SCORE,0,-1)
        if ip_ls:
            return random.choice(ip_ls)
        else:
            print("当前无可用的ip")

        



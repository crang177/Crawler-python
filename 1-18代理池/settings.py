#   配置当前项目的配置文件


#连接redis库
HOST="127.0.0.1"
PORT=6379
PASSWORD="123456"
DB=1

#   对于redis库中有序集合的配置
ZSET_NAME="proxy_redis" #   有序集合的名字
SCORE=100               #   初始权重
MIN_SCORE=70            #   最小权重设置
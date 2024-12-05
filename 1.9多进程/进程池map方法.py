from multiprocessing import Pool

import time

def run(i):
    print("我是子进程----",i)
    time.sleep(1)#运行的太快了，几乎看不到区别，使所以用这个来减慢速度，使得现象更明显

if __name__=="__main__":
    p=Pool(3)#开启的并发数（与cpu好像数有关，默认为本地的核心数）
    arg=[1,2,3,4,5,6,7]
    p.map(run,arg)
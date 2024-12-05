from multiprocessing import Pool,cpu_count
import time

def run(i):
    print("我是子进程----",i)
    time.sleep(1)#运行的太快了，几乎看不到区别，使所以用这个来减慢速度，使得现象更明显

if __name__=="__main__":
    print(f"我的cpu核心数量 :  {cpu_count()}")
    p=Pool()#开启的并发数（与cpu好像数有关，默认为本地的核心数）
    for i in range(1,20):
        p.apply_async(run,args=(i,))
    p.close()
    p.join()
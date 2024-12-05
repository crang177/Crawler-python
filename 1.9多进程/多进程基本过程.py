from multiprocessing import Process
import time

def task():
    print("da sha bi ")

if __name__=="__main__":
    print("aa")

    p=Process(target=task)#创建Process对象，创建子进程，target为子进程要运行的代码
    p.start()#启动子进程
    p.join()#阻塞主进程，使得主进程等待子进程运行完成后一起运行

    print("bb")

    

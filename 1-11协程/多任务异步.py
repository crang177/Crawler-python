import asyncio
import time

async def run(i):
    print("开始任务：",i)
    await asyncio.sleep(2)#阻塞当前协程，将控制权给回事件循环，去做其他可执行的协程，暂停这个协程的时间为2秒,这两秒的时间去做别的事情,如果没有其他的协程做，那就直接暂停两秒
                           #await停止当前程序，去执行await的中的协程


    print("over",i)

async def main1():#使用ensure_future
    task_list=[]
    for i in range(1,4):
        cor=run(i)#创建协程对象
        task=asyncio.ensure_future(cor)#封装成任务
        task_list.append(task)
    await asyncio.wait(task_list)  #wait把多任务的列表注册到时间循环上

async def main2():#使用create_task()方法来封装成协程对象
    task_list=[]
    for i in range(1,4):
        cor=run(i)
        task=asyncio.create_task(cor)
        task_list.append(task)
    await asyncio.wait(task_list)





if __name__=="__main__":
        
    loop=asyncio.get_event_loop()#创建一个事件循环
    loop.run_until_complete(main1())#把事件丢入循环中（即开始运行协程）


    

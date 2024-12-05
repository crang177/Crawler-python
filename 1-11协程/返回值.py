import asyncio
import time

async def run(i):
    print("开始任务：",i)
    await asyncio.sleep(2)#阻塞当前协程，将控制权给回事件循环，去做其他可执行的协程，暂停这个协程的时间为2秒,这两秒的时间去做别的事情,如果没有其他的协程做，那就直接暂停两秒
                           #await停止当前程序，去执行await的中的协程


    print("over",i)
    return i

async def main1():#使用ensure_future
    task_list=[]
    for i in range(1,4):
        cor=run(i)#创建协程对象
        task=asyncio.ensure_future(cor)#封装成任务
        task_list.append(task)

    done,pending=await asyncio.wait(task_list) #   wait有两个返回值：已完成的协程对象done和为完成的协程对象pending  (得到的都是列表)
    print(done)
    for r in done:
        print(r)
        print(r.result())#对于一个对象来说，使用result()方法来获返回值



async def main2():#使用create_task()方法来封住协程对象
    task_list=[]
    for i in range(1,4):
        cor=run(i)
        task=asyncio.create_task(cor)
        task_list.append(task)
    done=await asyncio.gather(*task_list)#使用gether（）方法得到返回值的列表，不是协程对象，*task—_list将列表拆分成元素带入
    for r in done:
        print(r)


def callback(f):
    print("callback",f.result())

async def main3():
    task_list=[]
    for i in range(1,4):
        cor=run(i)
        task=asyncio.create_task(cor)

        task.add_done_callback(callback)#添加回调
        task_list.append(task)
    await asyncio.wait(task_list)


if __name__=="__main__":
        
    loop=asyncio.get_event_loop()#创建一个事件循环
    loop.run_until_complete(main3())#把事件丢入循环中（即开始运行协程）


    

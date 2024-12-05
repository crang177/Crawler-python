import threading

#没有错乱的原因（新版本已经修改好了）
sum=0
def run1():
    global sum
    for i in range(100000):
        sum+=1
        sum-=1
    print(sum)


def run2():
    global sum
    for i in range(10):
        sum+=1
        sum-=1
    print(sum)


if __name__=="__main__":
    t1=threading.Thread(target=run1)
    t2=threading.Thread(target=run2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


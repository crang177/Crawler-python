from multiprocessing import Process,Manager,cpu_count


def run1(L):
    L.append("aa")
    L.append("77")
    L.append("rr")
    print(L)
    
def Manager_list():#传递列表
    List=Manager().list()
    P=Process(target=run1,args=(List,))
    P.start()
    P.join()
    print(List)




def run2(D):
    D["aa"]=112
    D["sda"]=565
    print(D)
    
def Manager_dict():#传递字典
    Dict=Manager().dict()
    P=Process(target=run2,args=(Dict,))
    P.start()
    P.join()
    print(Dict)





def run3(q):
    q.put("王凯太")#put（）放入数据，会自动换行
    q.put("大厦比")
    q.put("n")
    
    
def Manager_queue():#传递队列
    que=Manager().Queue()
    P=Process(target=run3,args=(que,))
    P.start()
    P.join()


    print(que.get())#得到数据，对应了上面put（）的次序，若队列中无值将会阻塞
    print(que.get())
    print(que.get())

    print(que.get(timeout=3))#超时参数设置


if __name__=="__main__":
    Manager_list()
    Manager_dict()
    Manager_queue()
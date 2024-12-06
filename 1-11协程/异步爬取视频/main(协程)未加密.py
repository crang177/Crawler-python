import aiohttp,aiofiles,os,time,asyncio,re
from aiohttp import TCPConnector
from pathlib import Path







#  这个函数用来获取下一个m3u8文件的地址，因为很多视频的.ts的url(可能不完整)会在下一个m3u8文件的response中
#  url           为第一个个m3u8文件的url
#  YuMing        为请求的网站
#  key           为除去域名和index.m3u8的中间部分的路径
#  YuMing,key    用来拼接ts的url
async def get_url(url,YuMing,key):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }

    async with aiohttp.ClientSession() as session :
        async with session.get(url,headers=headers) as res:
                                
            str=await res.text(encoding="utf-8")
            ls=str.split("\n")
            get_ts_url=f"https://{YuMing}/{key}/"+ls[2]
    await get_ts(get_ts_url,headers)#去请求下一个m3u8文件的地址，然后得到每个.ts文件的url  
   
    














#      去请求下一个m3u8文件的地址，然后得到每个.ts文件的url  
#      get_ts_url         为第二个m3u8文件的url     
async def get_ts(get_ts_url,headers):
    TsRegxes=re.compile(r'#EXTI.*?\n(.*)?.ts')#在访问的第二个m3u8文件的响应中去匹配.ts的文件

    async with aiohttp.ClientSession() as session :
        async with session.get(get_ts_url,headers=headers) as res:#请求第二个m3u8文件
            ts_str=await res.text(encoding="utf-8")#读取响应并把值赋给ts_str

            async with aiofiles.open("1-11协程/异步爬取视频/ts.txt","w",encoding="utf-8") as fp:#将响应写入.txt文件中，因为后面创建一个m3u8.m3u8文件，用来与下载来的ts文件进行匹配
                await fp.write(ts_str)

            print(res.status)
            ts_list=TsRegxes.findall(ts_str)

            ts_download_list=[]
            #拼接出ts文件的完整url
            for i in ts_list:
                ts_download_list.append(get_ts_url[:-10]+i+".ts")
 
    #将装有全部ts的url的列表拿去下载
    await ts_download_all(ts_download_list)














#  单个ts文件下载
#  url     为单个ts文件的url
#  name    为要给这个ts文件下载完成后的名字
#  sem     为协程并发控制量
async def downlao_one(url,name,sem):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }
    while True:

        # 使用信号量 控制并发
        async with sem:
            try :
                #connector=TCPConnector(ssl=False)用来当访问的网站的证书过期时  忽略弹出的警告
                async with aiohttp.ClientSession(connector=TCPConnector(ssl=False),headers=headers) as session :
                    #单个ts文件下载不超过60s
                    async with session.get(url,timeout=60) as res:#
                        data=await res.read()

                        async with aiofiles.open(f"1-11协程/异步爬取视频/ts/{name}","wb") as fp:
                            await fp.write(data)
                        print(url,"======下载成功")
                        break
            except:
                print(url,"======下载失败，正在重新下载")
    













 #    下载全部的ts文件，
 #   ts_download_list装有全部ts的url的列表  
async def ts_download_all(ts_download_list) :

    #协程并发控制
    sem=asyncio.Semaphore(200)
    task_list=[]#装任务得列表

    for i in range(len(ts_download_list)):
        #单个下载ts的任务（使用了线程），sem为协程并发控制数量，创建了cor对象
        cor=downlao_one(ts_download_list[i],    str(i)+".ts",   sem)

        task=asyncio.create_task(cor)#封装成任务
        task_list.append(task)#将任务添加到列表中
    
    #开始执行下载，等到一直所有都下载完了再进行下一步
    await asyncio.wait(task_list)
        










#    读取.txt中被写入的第二个m3u8响应，
#    此时创建一个ts.m3u8文件，里面的所有.ts文件的名字命名为0开始的.ts文件
#    创建的ts.m3u8文件必须与下载下来的ts文件在同一个文件夹中
def do_m3u8_url():
    with open("1-11协程/异步爬取视频/ts.txt","r") as fp:
        data=fp.readlines()#逐行读取数据，返回一个列表，一个元素代表一行的内容，包含了换行符

    f=open("1-11协程/异步爬取视频/ts/ts.m3u8","w") 
    i=0
    for line in data:
        if line[0]=="#":#用了区别是不是.ts文件
            f.write(line)
        else:
            f.write(f"{i}.ts\n")
            i+=1












#   使用fppmeg软件合并所有的ts的片段形成mp4文件
#   filename    为形成的mp4文件的名字
def merge(filename):
    '''
    进行ts文件合并 解决视频音频不同步的问题 建议使用这种
    :param filePath:
    :return:
    '''

    #    1-11协程/异步爬取视频/ts/ts.m3u8                为要合成文件对应下的ts.m3u8文件地址
    #    1-11协程/异步爬取视频/视频/{filename}.mp4        为合成完成后的路径和名字（包括格式）
    cmd = f'ffmpeg -i 1-11协程/异步爬取视频/ts/ts.m3u8 -c copy 1-11协程/异步爬取视频/视频/{filename}.mp4'
    # 执行合并命令
    os.system(cmd)


       










#  用于删除合成完成后的ts片段文件
def  delate_ts() :
    os.unlink("1-11协程/异步爬取视频/ts/ts.m3u8")

    if  os.listdir("1-11协程/异步爬取视频/ts"):  #   os.listdir（）获取某文件夹中的所有文件（包含文件夹）的名字，返回一个列表
        for i in Path("1-11协程/异步爬取视频/ts").glob('*.ts'):#  匹配所有的.ts文件
            os.unlink(i)#删除对应的.ts文件，永久删除


    
                   
    









async def main():
    
    url=input("输入m3u8地址: ")
    #https://v3.dious.cc/20220329/3yZIuUAL/index.m3u8
    name=input("名字：")
    regexes=re.compile(r'^https://(.*?)/(.*)?/index.m3u8',re.VERBOSE)  #用来分隔域名和后面的部分,例如 v3.dious.cc 和 20220329/3yZIuUAL，因为不同网站的域名和不同视频的后面部分不一样
    ls=regexes.findall(url)
    YuMing,key=ls[0]  #YuMing代表域名，key表示后面的路径即不包含域名和/index.m3u8部分的路径
    
    
    
    print("开始爬取")
    #开始爬去和下载对应数据
    await get_url(url,YuMing,key)
    #创建一个ts.m3u8文件，并且写入对应关系
    do_m3u8_url()
    #合成ts片段为视频
    merge(filename=name)
    #删除不需要再使用的.ts文件
    delate_ts()





if __name__=="__main__":
    asyncio.run(main())
    

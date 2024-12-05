import aiohttp,aiofiles,os,time,asyncio,re,requests
from aiohttp import TCPConnector
from pathlib import Path


async def get_url(url,YuMing,key):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }

    async with aiohttp.ClientSession() as session :
        async with session.get(url,headers=headers) as res:
                                
            str=await res.text(encoding="utf-8")
            ls=str.split("\n")
            if key in ls[2]:
                get_ts_url=f"https://{YuMing}"+ls[2]
            else:
                get_ts_url=f"https://{YuMing}/{key}/"+ls[2]
    await get_ts(get_ts_url,headers,YuMing,key)     
   
    

async def get_ts(get_ts_url,headers,YuMing,key):
    TsRegxes=re.compile(r'#EXTI.*?\n(.*)?.ts')
    async with aiohttp.ClientSession() as session :
        async with session.get(get_ts_url,headers=headers) as res:
            ts_str=await res.text(encoding="utf-8")
                
            async with aiofiles.open("1-11协程/异步爬取视频/ts.txt","w",encoding="utf-8") as fp:
                await fp.write(ts_str)
            print(res.status)
            ts_list=TsRegxes.findall(ts_str)
            ts_download_list=[]
            for i in ts_list:
                if key in i:
                    ts_download_list.append(f"https://{YuMing}"+i+".ts")
                else:
                    ts_download_list.append(get_ts_url[:-10]+i+".ts")
 
    
    await ts_download_all(ts_download_list)
    
    if "URI=" in ts_str:
        regexes=re.compile(r'URI="(.*)?"')
        ls=regexes.findall(ts_str)
        key_url=f"https://{YuMing}"+ls[0]
        get_key(key_url,headers)
        global key_num
        global key_str
        key_num=1
        key_str=ls[0]
        




async def downlao_one(url,name,sem):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }
    while True:
        async with sem:
            try :
                async with aiohttp.ClientSession(connector=TCPConnector(ssl=False),headers=headers) as session :
                    async with session.get(url,timeout=60) as res:
                        data=await res.read()

                        async with aiofiles.open(f"1-11协程/异步爬取视频/ts/{name}","wb") as fp:
                            await fp.write(data)
                        print(url,"======下载成功")
                        break
            except:
                print(url,"======下载失败，正在重新下载")
    

            
async def ts_download_all(ts_download_list) :
    sem=asyncio.Semaphore(200)
    task_list=[]
    for i in range(len(ts_download_list)):
        cor=downlao_one(ts_download_list[i],    str(i)+".ts",   sem)
        task=asyncio.create_task(cor)
        task_list.append(task)
    await asyncio.wait(task_list)
        
def do_m3u8_url(*url):
    with open("1-11协程/异步爬取视频/ts.txt","r") as fp:
        data=fp.readlines()
    f=open("1-11协程/异步爬取视频/ts/ts.m3u8","w",encoding="utf-8") 
    i=0
    for line in data:
        if line[0]=="#":
            if "URI=" in line:
                line=line.replace(url[0],"key.m3u8")


            
            f.write(line)
        else:
            f.write(f"{i}.ts\n")
            i+=1

def merge(filename):
    '''
    进行ts文件合并 解决视频音频不同步的问题 建议使用这种
    :param filePath:
    :return:
    '''
    cmd = f'ffmpeg -i 1-11协程/异步爬取视频/ts/ts.m3u8 -c copy 1-11协程/异步爬取视频/视频/{filename}.mp4'
    # 执行合并命令
    os.system(cmd)

         

def delate_ts():
    os.unlink("1-11协程/异步爬取视频/ts/ts.m3u8")
    if  os.listdir("1-11协程/异步爬取视频/ts"):
        for i in Path("1-11协程/异步爬取视频/ts").glob('*.ts'):
            os.unlink(i)


def get_key(url,headers):
    res=requests.get(url,headers)
    res.encoding=res.apparent_encoding
    with open ("1-11协程/异步爬取视频/ts/key.m3u8","w",encoding="utf-8") as  fp:
        fp.write(res.text)
    

                   
    


async def main():
    
    url=input("输入m3u8地址: ")
    name=input("名字：")
    regexes=re.compile(r'^https://(.*?)/(.*)?/index.m3u8',re.VERBOSE)

    ls=regexes.findall(url)
    YuMing,key=ls[0]
    
    
    
    print("开始爬取")
    await get_url(url,YuMing,key)

    if key_num==0:
        do_m3u8_url()
    else:
        do_m3u8_url(key_str)
    merge(filename=name)
    delate_ts()



if __name__=="__main__":
    key_num=0
    key_str=''
    asyncio.run(main())
    

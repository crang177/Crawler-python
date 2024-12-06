import aiohttp,aiofiles,os,time,asyncio,re,requests
from aiohttp import TCPConnector
from pathlib import Path
"""
    这个代码的大体功能跟无加密的代码一样
    只需要注意这点：
        访问第二个m3u8文件中存在   #EXT-X-KEY:METHOD=AES-128,URI="/20220329/3yZIuUAL/2000kb/hls/key.key"  
            即EXT-X-KEY 和 URI 说明下载的数据经过了加密
            可能#EXT-X-KEY:METHOD=AES-128,URI="/20220329/3yZIuUAL/2000kb/hls/key.key"  中后面还包括偏移量IV，处理办法一样

        解决办法：
            1.(在第二个m3u8文件的响应中)将  #EXT-X-KEY:METHOD=AES-128,URI="/20220329/3yZIuUAL/2000kb/hls/key.key"  中的 URI的值扣出来,然后根据域名等等,拼接成一个url，
                    这个url就是密钥的url,响应的值就是密钥。  如果存在偏移量IV的具体值不用理会,fppmeg会自动帮我们解密数据
                  
            2.访问 1 中得到的url, 创建一个名为  key.m3u8 的文件(这个文件也必须放在下载的ts的文件夹中)  ，将得到的响应写入 key.m3u8 这个文件中

            3.在do_m3u8_url(*url)这个函数创建ts.m3u8文件时(其实和txt中的文件一样,只是把.ts的名字根据上到下的顺序重新命名为 0.ts ,  1.ts等), 
                    把  #EXT-X-KEY:METHOD=AES-128,URI="/20220329/3yZIuUAL/2000kb/hls/key.key" 的 URI 的值改为 key.m3u8 
                    即  #EXT-X-KEY:METHOD=AES-128,URI="key.m3u8"  ,然后在写入到  ts.m3u8  文件中
"""






async def get_url(url,YuMing,key):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }

    async with aiohttp.ClientSession() as session :
        async with session.get(url,headers=headers) as res:
                                
            str=await res.text(encoding="utf-8")
            ls=str.split("\n")
            if "https://"  in ls[2]:
                get_ts_url=ls[2]
                
            elif key in ls[2]:
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
                if key in i:#主要作用就是根据第二个m3u8网站的响应中ts文件的url的完整程度来拼接url
                            #比如： 有些返回的 url   是完整的url，可以直接访问
                            #                 url   不完整，但是只是缺少了域名
                            #                 url   不完整，既缺少了域名，又缺少了部分中间的路径
                    ts_download_list.append(f"https://{YuMing}"+i+".ts")
                else:
                    ts_download_list.append(get_ts_url[:-10]+i+".ts")

    await ts_download_all(ts_download_list)
    
    #  根据URI是否在第二个m3u8文件中，判断是不是为加密数据
    if "URI=" in ts_str: #
        regexes=re.compile(r'URI="(.*)?"')#这个正则用来获取 #EXT-X-KEY:METHOD=AES-128,URI="/20220329/3yZIuUAL/2000kb/hls/key.key" 中的  /20220329/3yZIuUAL/2000kb/hls/key.key 
        ls=regexes.findall(ts_str)

        #构造key密钥的url
        key_url=f"https://{YuMing}"+ls[0]
        #访问密钥的url来获取密钥
        get_key(key_url,headers)
        global key_num
        global key_str
        key_num=1 #数据加密时，将全局变量设置为 1 
        key_str=ls[0] #数据加密时，得到  #EXT-X-KEY:METHOD=AES-128,URI="/20220329/3yZIuUAL/2000kb/hls/key.key" 中的  /20220329/3yZIuUAL/2000kb/hls/key.key 
                      #   拿来作为被替换的字符串，并且作为可选参数传递到do_m3u8_url(*url)中
        











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
        








#   *url  为可选参数，为  #EXT-X-KEY:METHOD=AES-128,URI="/20220329/3yZIuUAL/2000kb/hls/key.key" 中的  /20220329/3yZIuUAL/2000kb/hls/key.key 
#   拿来作为被替换的字符串
def do_m3u8_url(*url):
    with open("1-11协程/异步爬取视频/ts.txt","r") as fp:
        data=fp.readlines()
    f=open("1-11协程/异步爬取视频/ts/ts.m3u8","w",encoding="utf-8") 
    i=0
    for line in data:
        if line[0]=="#":
            if "URI=" in line:
                line=line.replace(url[0],"key.m3u8") # 字符串的替换方法    一个字符串.replace(被替换的字符串，要替换成什么字符串)  : 两个参数
                                                     #    str.replace(hello , bye)  : 将str字符中的所有 hello字符串全部替换成 bye字符串


            
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












#列子网址1：https://wwqp47.art/vodplay/363448-1-1.html的m3d8
#         https://v3.dious.cc/20220329/3yZIuUAL/index.m3u8
if __name__=="__main__":

    #这两个值将被使用为全局变量
    key_num=0   #如果为 0 ，说明数据未加密，为1 说明数据加密了
    key_str=''  #  这个就是为  #EXT-X-KEY:METHOD=AES-128,URI="/20220329/3yZIuUAL/2000kb/hls/key.key" 中的  /20220329/3yZIuUAL/2000kb/hls/key.key 
                #   拿来作为被替换的字符串，如果为加密的话就是一个空字符串
    asyncio.run(main())
    

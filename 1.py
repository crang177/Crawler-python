import re,os
from pathlib import Path
def delate_ts():
    #os.unlink("1-11协程/异步爬取视频/ts/ts.m3u8")
    if  os.listdir("1-11协程/异步爬取视频/ts"):
        for i in Path("1-11协程/异步爬取视频/ts").glob('*.ts'):

            os.unlink(i)
# line=re.sub("/20220329/3yZIuUAL/2000kb/hls/key.key","1-11协程/异步爬取视频/ts/key.m3u8",'#EXT-X-KEY:METHOD=AES-128,URI="/20220329/3yZIuUAL/2000kb/hls/key.key"')
# print(line)


# def do_m3u8_url(*url):
#     with open("1-11协程/异步爬取视频/ts.txt","r") as fp:
#             data=fp.readlines()
#     f=open("1-11协程/异步爬取视频/ts/ts.m3u8","w",encoding="utf-8") 
#     i=0
#     for line in data:
#         if line[0]=="#":
#             if "URI=" in line:
                
#                 line=line.replace(url[0],"key.m3u8")


            
#             f.write(line)
#         else:
#             f.write(f"{i}.ts\n")
#             i+=1
# do_m3u8_url("/20220329/3yZIuUAL/2000kb/hls/key.key")


# def merge(filename):
#     '''
#     进行ts文件合并 解决视频音频不同步的问题 建议使用这种
#     :param filePath:
#     :return:
#     '''
#     cmd = f'ffmpeg -i 1-11协程/异步爬取视频/ts/ts.m3u8 -c copy 1-11协程/异步爬取视频/视频/{filename}.mp4'
#     # 执行合并命令
#     os.system(cmd)

# merge(filename="2")

delate_ts()
import os ,shutil,re


os.system("cls")
regexes=re.compile(r'(.*)?-\[.*.mp4')
#ls=os.listdir("D:/DownKyi-1.0.16-1.win-x64/Media/STM32入门教程-2023版 细致讲解 中文字幕")
ls=os.listdir("D:/DownKyi-1.0.16-1.win-x64/Media/新建文件夹")

for i in ls :

    num=int(regexes.findall(i)[0])


    old="D:/DownKyi-1.0.16-1.win-x64/Media/新建文件夹/"+i
    if num<10:
        new="D:/stm32/视频/"+i[2:-17]+".mp4"
    else:
        new="D:/stm32/视频/"+i[3:-17]+".mp4"
    shutil.move(old,new)
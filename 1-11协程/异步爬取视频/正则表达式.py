import re,os


os.system("cls")
TsRegxes=re.compile(r'#EXTI.*?\n(.*)?.ts')
with open("1-11协程/异步爬取视频/ts.txt") as fp:
    str=fp.read()
ls=TsRegxes.findall(str)
for i in ls:
    print(i)


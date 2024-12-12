import os,asyncio,aiohttp,re
from lxml import etree
from pymongo import MongoClient

def increase_data(ls):
    conn=MongoClient("localhost")
    db=conn.study
    for i in ls:
        db.user.insert_one(i)
    conn.close()
 


async def get_data_url(url):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as res:
                print(res.status)
                selector=etree.HTML(await res.read())
    ls=selector.xpath("//dd/ul/li")[:20]
    task_web_list=[asyncio.create_task(get_data( url='https://www.xigushi.com'+i.xpath("./a/@href")[0]))  for i in ls]
    await asyncio.wait(task_web_list)
    
  
async def get_data(url):
   
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as res:
           
            text=await res.text()

            selector=etree.HTML(text)


            ls=selector.xpath('//div[@class="by"]/dl//dd')
            regexes=re.compile(r'时间:.*作者:(.*)? 编辑:')
            for i in ls:
                title=i.xpath('./h1/text()')[0]
                author=regexes.findall(i.xpath("./div/text()")[0])[0]        
                body_ls=i.xpath("./p/text()")
                body=''.join(body_ls)
                body=body.replace('\r','').replace("\n",'').replace("\u3000",'')
                task_ls.append({"title":title,"author":author,"body":body})



        
        
        

async def main():
    os.system("cls")
    print("开始爬取")
    url="https://www.xigushi.com/mrgs/"
    await get_data_url(url)
    print("爬取完成")
    print("开始写入数据")
    increase_data(task_ls)
    print("数据写入完成")
    



if __name__=="__main__":
    os.system("cls")
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Referer":"https://www.xigushi.com/",
    }
    task_ls=[]
    
    asyncio.run(main())
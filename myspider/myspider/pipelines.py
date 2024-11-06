# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class MyspiderPipeline:#这个是初始的管道
    def __init__(self):#为什么将打开文件放在这里，因为yield有很多个，process_item(self, item, spider)就要运行多少次，如果
                       #放在process_item(self, item, spider)中就会打开多少次文件
        self.file=open("itcast.json","w")
    def process_item(self, item, spider):#yield每返回一个值就给到item，然后运行一次管道，spider为当前运行的爬虫
        #将字典数据进行j序列化，ensure_ascii=False用于显示中文字符，默认为True,则是使用byte类写入数据
        item=dict(item)
        json_data=json.dumps(item,indent=4,ensure_ascii=False)+",\n"#因为数据是一个一个进入管道，所以可以用，\n来对下一个数据进行分隔


        self.file.write(json_data)

        #默认使用管道后要将数据返回给到引擎
        return item
    def __closefile__(self) :
        self.file.close()
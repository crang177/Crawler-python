import scrapy
from myspider.items import MyspiderItem

class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]#允许的域名
    start_urls = ["https://www.itheima.com/teacher.html#ajavaee?cz-pc-dh}"]#起始url，将会自动的发送请求

    def parse(self, response):#解析数据，将其实的url的自动发送的请求的对应的响应进行解析，起始的解析方法
        # with open("itcast.html","wb") as f:
        #     f.write(response.body)
        #获取的是所有教师的节点
        t_list=response.xpath('//div[@class="li_txt"]')

        #teacher_list=[]
        #遍历教师列表的节点，利用节点的xpath对数据进行提取
        for t in t_list:
            temp=MyspiderItem()
            #xpath返回的是选择器对象列表
            temp["name"]=t.xpath('./h3/text()').extract_first()#extract_first将选择器对象中的数据提取出来，当选择器列表中只有一个值的时候可以有fist，有多值的时候就不可以
            temp["position"]=t.xpath('./h4/text()').extract_first()
            temp["information"]=t.xpath('./p/text()').extract_first()
            #teacher_list.append(temp)
            yield temp #使用yield返回值可以不终止函数，也适用于翻页
            
            
        

        


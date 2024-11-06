# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()#讲师的名字
    position=scrapy.Field()#讲师的职位
    information=scrapy.Field()#讲师的简介
    

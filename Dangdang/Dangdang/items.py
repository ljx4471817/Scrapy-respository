# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field() #书名
    url = scrapy.Field() #购买链接
    comment = scrapy.Field() #评论数
    price = scrapy.Field() #价格
    ranking = scrapy.Field() #同类书排名


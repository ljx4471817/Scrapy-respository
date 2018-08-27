# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from qianchenwuyou.items import QianchenwuyouItem
import re

class QcwySpider(scrapy.Spider):
    name = 'qcwy'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/260200,000000,0000,00,9,99,python,2,1.html']

    def parse(self, response):
        for i in range(1, 3):
            url = 'https://search.51job.com/list/260200,000000,0000,00,9,99,python,2,' + str(i) + '.html'

            yield Request(url, self.geturl)

    def geturl(self, response):
        print('进来')
        print(response.url)
        url = response.xpath('//div[@class="el"]/p/span/a/@href').extract()  # 每个岗位的链接
        for i in url:
            yield Request(i, self.getdata)

    def getdata(self, response):
        items = QianchenwuyouItem()
        items['Job_title'] = response.xpath('//h1/@title').extract()
        items['Company'] = response.xpath('//p[@class="cname"]/a/@title').extract()
        items['Salay']=response.xpath('//div[@class="cn"]/strong/text()').extract()
        items['Details'] = response.xpath('//div[@class="bmsg job_msg inbox"]').extract()
        items['Details']=re.sub('<div class="bmsg job_msg inbox">\r\n\t\t\t\t\t\t','',items['Details'][0])#数据整理,去除无意义内容
        items['Details']=re.sub('<.*?>','',items['Details'])#数据整理,去除各种<>标签
        items['Details'] = re.sub('\s', '', items['Details'])#数据整理,去除空白字符
        items['WorkLocation'] = response.xpath('//div[@class="bmsg inbox"]/p/text()').extract()
        items['WorkLocation'] = re.sub('\s','',items['WorkLocation'][1])# 数据整理,去除空白字符
        items['Company_introduce']=response.xpath('//div[@class="tmsg inbox"]/text()').extract()
        items['Company_introduce'] = re.sub('\s', '', items['Company_introduce'][0])  # 数据整理,去除空白字符
        yield items


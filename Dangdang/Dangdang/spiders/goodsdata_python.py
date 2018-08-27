# -*- coding: utf-8 -*-
import scrapy
from Dangdang.items import DangdangItem
from scrapy.http import Request
import re

class GoodsdataPythonSpider(scrapy.Spider):

    name = 'goodsdata_python'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=python&act=input&page_index=1']

    def parse(self, response):
        for i in range(1,10):
            #爬虫范围 前10页
            url = 'http://search.dangdang.com/?key=python&act=input&page_index='+str(i)
            yield Request(url,self.in_parse)


    #每一页中数据
    #next:进入每个商品页面
    def in_parse(self,response):
        #每个商品的购买链接
        url = response.xpath('//a[@dd_name="单品图片"]/@href').extract() #链接
        title=response.xpath('//a[@dd_name="单品图片"]/@title').extract() #标题
        price = response.xpath('//span[@class="search_now_price"]/text()').extract()#价格
        for i in range(len(url)):
            yield Request(url[i],callback=self.single_goods,meta={'title':title[i],'price':price[i]})

    #每个商品购买页面
    def single_goods(self,response):
        item = DangdangItem()
        item['title']=response.meta['title'] #商品名
        item['url']=response.url #购买链接
        item['comment']=response.xpath('//a[@dd_name="评论数"]/text()').extract() #评论数
        item['price']=response.meta['price']#价格
        # 商品id,为获得商品排名
        goods_id = str(item['url']).split('/')
        g_id = goods_id[len(goods_id)-1].split('.')[0]
        ranking_url='http://product.dangdang.com/index.php?r=callback%2Fget-bang-rank&productId='+g_id
        yield Request(ranking_url,self.getrank,meta={'item':item})

# 同类书籍排名统计
    def getrank(self,response):
        item = DangdangItem()
        item=response.meta['item']
        if len(response.text)>100:
            item['ranking'] =re.findall('"rank":"(.*?)"',response.text)[0]
        else:
            item['ranking']='无排名'
        return item

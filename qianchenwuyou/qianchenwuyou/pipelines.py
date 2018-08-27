# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QianchenwuyouPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='spiderdata')
        Job_title=item['Job_title'][0]
        Company=item['Company'][0]
        Salay=item['Salay'][0]
        Details=item['Details']
        WorkLocation=item['WorkLocation']
        Company_introduce=item['Company_introduce']

        sql = "insert into qcwy(Job_title,Company,Salay,Details,WorkLocation,Company_introduce) values('"+Job_title+"','"+Company+"','"+Salay+"','"+Details+"','"+WorkLocation+"','"+Company_introduce+"')"
        print(sql)
        conn.query(sql)
        conn.commit()
        print('关闭数据库')
        conn.close()
        return item



    # Job_title = scrapy.Field() #岗位名称
    # Company = scrapy.Field() #公司名称
    # Salay = scrapy.Field() #薪酬
    # Details = scrapy.Field() #职位详情
    # WorkLocation = scrapy.Field() #公司地址
    # Company_introduce = scrapy.Field() #公司简介
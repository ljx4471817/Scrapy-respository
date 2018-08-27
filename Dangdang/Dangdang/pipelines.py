# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):

    print('数据库连接建立!')
    def process_item(self, item, spider):
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='spiderdata')
        print('DangdangPipelineitem:',item)
        title=item['title']
        url = item['url']
        price = item['price']
        ranking=item['ranking']
        comment=item['comment']
        if len(comment)==1:
            comment=comment[0]
        else:
            comment=0
        sql = "insert into dangdang(title,url,comment,price,ranking) values('"+title+"','"+url+"','"+str(comment)+"','"+price+"','"+str(ranking)+"')"

        print(sql)
        conn.query(sql)
        conn.commit()
        print('关闭数据库')
        conn.close()
        return item


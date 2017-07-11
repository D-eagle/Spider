# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BookingPipeline(object):
    def process_item(self, item, spider):
    	print "--------------------------------"
        print u'【名称】：'+item['name'][0]
        print u'【作者】：'+item['author'][0]
        print u'【出版社】：'+item['publish'][0]
        print u'【价格】：'+item['price']
        #print u'【货源】：'+item['goods'][0]
        #print u'【折扣】：'+item['discount'][0]
        print u'【链接】：'+item['link']
        print "--------------------------------"
        return item

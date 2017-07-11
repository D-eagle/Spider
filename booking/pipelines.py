# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BookingPipeline(object):
    def process_item(self, item, spider):
    	print "--------------------------------"
        print item['name'][0]+u'/n'
        print item['author'][0]+u'/n'
        print item['publish'][0]+u'/n'
        print item['price'][0]+u'/n'
        print item['goods'][0]+u'/n'
        print item['discount'][0]+u'/n'
        print item['link'][0]+u'/n'
        print "--------------------------------"
        return item

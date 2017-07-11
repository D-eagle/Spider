# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    publish = scrapy.Field()
    price = scrapy.Field()
    goods = scrapy.Field()
    discount = scrapy.Field()
    link = scrapy.Field()    

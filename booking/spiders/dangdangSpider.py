# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from booking.items import BookingItem

class MySpider(scrapy.Spider):
	"""docstring for MySpider"""
	name = 'dangdangspider'
	allowed_domains = ['dangdang.com']
	def __init__(self, category=None, *args, **kwargs):
		super(MySpider, self).__init__(*args, **kwargs)
		self.start_urls = [u'http://search.dangdang.com/?key=%s&act=input' % category]
		# ...
	
	def parse(self,respones):
		url_list = respones.xpath('//p[@class="name"]//@href').extract()
		for url in url_list:
			yield Request(url,callback = self.parse_name) 
		# for i in range(2,5):
		# 	page_url = u'http://search.dangdang.com/?key=%C5%ED%B3%CA%B2%D6&act=input'.format(i)
		# 	yield Request(page_url,callback = self.parse)

	def parse_name(self,respones):
		items = BookingItem()
		items['name'] = respones.xpath('//div[@class="name_info"]/h1/@title').extract()
		items['author'] = respones.xpath('//span[@id="author"]/a/@text()').extract()
		items['publish'] = respones.xpath(u'//span[@dd_name="出版社"]/a/@text()').extract()
		items['price'] = respones.xpath('//div[@class="price_pc"]//p[@id="dd-price"]/text()').extract()
		items['goods'] = respones.xpath('//div[@class="area_pop"]/b/@text()').extract()
		items['discount'] = respones.xpath('//div[@class="price_zhe"]/@text()').extract()
		items['link'] = respones.url
		yield items

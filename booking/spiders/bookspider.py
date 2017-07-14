# -*- coding: utf-8 -*-
import scrapy
import urllib2
import re
from scrapy.http import Request
from booking.items import BookingItem


class MySpider(scrapy.Spider):
	"""docstring for MySpider"""
	name = 'bookspider'
	allowed_domains = ['dangdang.com']
	def __init__(self, category=None, *args, **kwargs):
		super(MySpider, self).__init__(*args, **kwargs)
		keyword = urllib2.quote(category)
		self.start_urls = [u'http://search.dangdang.com/?key=%s&act=input' % keyword]
		print keyword
		# ...
	
	def parse(self,respones):
		url_dangdanglist = respones.xpath('//p[@class="name"]//@href').extract()
		for url in url_dangdanglist:
			yield Request(url,callback = self.parse_dangdang)
		# if re.match(r'jd.com','respones.url').group():
		# 	url_jdlist = respones.xpath('//a[target="_blank"]/@href').extract()
		# 	for url in url_jdlist:
		# 		yield Request(url,callback = self.parse_jd)

		# for i in range(2,5):
		# 	page_url = u'http://search.dangdang.com/?key=%C5%ED%B3%CA%B2%D6&act=input'.format(i)
		# 	yield Request(page_url,callback = self.parse)

	def parse_dangdang(self,respones):
		items = BookingItem()
		items['name'] = respones.xpath('//div[@class="name_info"]/h1/@title').extract()
		items['author'] = respones.xpath('//span[@id="author"]/a/text()').extract()
		items['publish'] = respones.xpath(u'//span[@dd_name="出版社"]/a/text()').extract()
		items['price'] = respones.xpath(u'//p[@id="dd-price"]/text()').extract()[1]
		#items['goods'] = respones.xpath('//div[@class="select_add clearfix"]/b/text())').extract()[1]
		#items['discount'] = respones.xpath('//div[@class="price_zhe"]').extract()
		items['link'] = responses.url
		yield items

	# def parse_jd():
	# 	items = BookingItem()
		

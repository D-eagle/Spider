# -*- coding: utf-8 -*-
import scrapy
import urllib2
import re
from scrapy.http import Request
from booking.items import BookingItem

class jdspider(scrapy.Spider):
	name = 'jdspider'
	allowed_domains = ['jd.com']
	start_urls = ['https://search.jd.com/Search?keyword=python&enc=utf-8']
	header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
	meta = {'dont_redirect': True,'handle_httpstatus_list': [301, 302]}
	# def __init__(self, category=None, *args, **kwargs):
	# 	super(MySpider, self).__init__(*args, **kwargs)
	# 	#exchange keyword into unicode 
	# 	keyword = urllib2.quote(category)
	# 	self.start_urls = [u'https://search.jd.com/Search?keyword=%s&enc=utf-8' % keyword]
	# 	print keyword
	def start_requests(self):
		yield Request(self.start_urls[0], callback = self.parse_name, headers = self.header, meta = self.meta)



	def parse_name(self,response):
		url_list = response.xpath('//div[@class="p-img"]/a/@href').extract()
		# print '#################'+url_list[0]+'#####################'
		# Request(self.start_urls[0], callback = self.parse_extractor)
		for url in url_list:
			url = 'https:' + url
			yield Request(url, callback = self.parse_extractor)

	def parse_extractor(self,response):
		items = BookingItem()
		publish = ''
		items['name'] = response.xpath('//div[@id="name"]/h1/text()').extract()
		items['author'] = response.xpath('//div[@class="p-author"]/a/text()').extract()
		
		#get publish name
		publish_name = response.xpath('//meta[@name="description"]/@content').extract()
		publish_compile = ur'\u51fa\u7248\u793e\uff1a(.*)\u3002\u4e70\u56fe\u4e66'
		publish = re.findall(publish_compile,publish_name[0])
		items['publish'] = publish

		#get price from js
		get_url = response.xpath('//a[@class="report-btn"]/@href').extract()
		skuId = re.findall(ur'skuId=(.*)',get_url[0])
		price_url = 'https://p.3.cn/prices/get?skuid=J_'+skuId[0]
		req = urllib2.Request(price_url,headers = self.header)
		req_body = urllib2.urlopen(req).read()
		items['price'] = re.findall(r'"p":"(.*)"',req_body)#'
		#items['goods'] = respones.xpath('//div[@class="select_add clearfix"]/b/text())').extract()[1]
		# items['discount'] = response.xpath('//span[@class="p-discount"]/text()').extract()
		
		items['link'] = response.url

		yield items

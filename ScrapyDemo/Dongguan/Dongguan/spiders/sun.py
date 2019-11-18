# -*- coding: utf-8 -*-
import scrapy

# 制作爬虫

class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['sun.com']
    start_urls = ['http://sun.com/']

    def parse(self, response):
        pass

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DouyuspiderItem(scrapy.Item):
    name = scrapy.Field()
    imagesUrls = scrapy.Field()
    imagesPath = scrapy.Field()

class Demo1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

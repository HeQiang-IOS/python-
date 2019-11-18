# -*- coding: utf-8 -*-
import scrapy

from mySpider.items import ItcastItem

# 制作爬虫
# 1、抓数据

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # filename = "teacher.html"
        # open(filename, 'wb').write(response.body)

        # 存放老师信息的集合
        # items = []
        # response = response.decode('utf-8')
        for each in response.xpath("//div[@class='li_txt']"):
            item = ItcastItem()

            name = each.xpath("h3/text()").extract()
            title = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()

            item['name'] = name[0]
            item['level'] = title[0]
            item['info'] = info[0]

            # items.append(item)

            # 将获取的数据交给pipelines
            yield item

        # return items

"""
class renrenSpider(scrapy.spiders):

    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'

        # FormRequest 是Scrapy发送POST请求的方法
        yield scrapy.FormRequest(
            url=url,
            formdata={"email": "mr_mao_hacker@163.com", "password": "axxxxxxxe"},
            callback=self.parse_page
        )

    def parse_page(self, response):
# do something

"""
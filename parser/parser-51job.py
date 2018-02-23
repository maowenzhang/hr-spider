'''
Created on Oct 21, 2017

@author: zhanglo
'''

import scrapy

class MySpider51Job(scrapy.Spider):
    '''
    classdocs
    '''
    name = 'mySpider'
    start_urls = ['http://www.baidu.com']
    
    def parse(self, response):
        for title in response.css('h2.entry-title'):
            yield {'title' : title.css('a ::text').extract_first() }

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)
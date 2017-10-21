'''
Created on Oct 21, 2017

@author: zhanglo
'''

import scrapy

class MySpider(scrapy.spider):
    '''
    classdocs
    '''
    name = 'mySpider'
    start_urls = ['http://www.baidu.com']
    
    name = 'testSpider'
    start_urls = ['https://www.baidu.com']
    
    def __init__(self, params):
        '''
        Constructor
        '''
        
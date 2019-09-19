# -*- coding: utf-8 -*-
import scrapy


class NbastatsSpider(scrapy.Spider):
    name = 'nbastats'
    allowed_domains = ['stats.nba.com']
    start_urls = ['http://stats.nba.com/']

    def parse(self, response):
        pass

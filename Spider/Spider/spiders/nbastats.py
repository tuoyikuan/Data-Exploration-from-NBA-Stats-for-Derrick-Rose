# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin, urlencode

class NbastatsSpider(scrapy.Spider):
    name = 'nbastats'
    allowed_domains = ['stats.nba.com']
    base = 'http://stats.nba.com/player/'
    player_id = '201565/'
    data_type = 'shots-dash/'
    years = range(16, 18)
    url = urljoin(base, player_id+data_type)
    start_urls = []
    for year in years:
        parameters = {
            'Season' : '20'+str(year)+'-'+str(year+1),
            'SeasonType' : 'Regular Seanson'
        }
        start_urls.append(urljoin(url,'?'+urlencode(parameters)))
    # print(start_urls)



    def parse(self, response):


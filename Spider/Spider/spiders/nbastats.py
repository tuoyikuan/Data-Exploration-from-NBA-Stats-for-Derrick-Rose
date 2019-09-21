# -*- coding: utf-8 -*-
import scrapy
import json
from urllib.parse import urljoin, urlencode

class NbastatsSpider(scrapy.Spider):
    name = 'nbastats'
    # allowed_domains = ['stats.nba.com']
    # base = 'https://stats.nba.com/player/'
    # player_id = '201565/'
    # data_type = 'shots-dash/'
    # years = range(16, 18)
    # url = urljoin(base, player_id+data_type)
    start_urls = ['https://stats.nba.com/stats/playerdashptshots?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PerMode=PerGame&Period=0&PlayerID=201565&Season=2013-14&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision=']
    # for year in years:
    #     parameters = {
    #         'Season' : '20'+str(year)+'-'+str(year+1),
    #         'SeasonType' : 'Regular Seanson'
    #     }
    #     start_urls.append(urljoin(url,'?'+urlencode(parameters)))
    # print(start_urls)



    def parse(self, response):
        pass



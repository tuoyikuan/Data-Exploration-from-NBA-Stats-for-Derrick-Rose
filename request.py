import requests
import json

response = requests.get(url='https://stats.nba.com/stats/playerdashptshots?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PerMode=PerGame&Period=0&PlayerID=201565&Season=2013-14&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision=',
                   headers={
                        'Host': 'stats.nba.com',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
                        'Accept': 'application/json, text/plain, */*',
                        'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
                        'Accept-Encoding': 'gzip, deflate, br',
                         })
print(json.loads(response.text))

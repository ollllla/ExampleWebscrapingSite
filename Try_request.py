from urllib.request import urlopen, requests

url = 'http://stats.nba.com/stats/playerdashptshots?DateFrom=&DateTo=&GameSegment=&LastNGames=6&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PerMode=PerGame&Period=0&PlayerID=2544&Season=2017-18&SeasonSegment=&SeasonType=Playoffs&TeamID=0&VsConference=&VsDivision='

res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
for item in res.json()['resultSets']:
    if item['name'] == "ClosestDefender10ftPlusShooting":
        print(item['headers'])
        for items in item['rowSet']:
            print(items)

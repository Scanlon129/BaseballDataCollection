'''
Written by: Matt Scanlon
Written on: 2022-07-31 9:30 PM
Last Updated by: Matt Scanlon
Last Updated on: 2024-07-08 7:30 PM

Generated by insomnia in a few steps:
 - navigate to page
 - right click element - inspect
 - select network -> Fetch/XHR
 - refresh page
 - select last 7 days
 - Find GET request (right click table and select method if needed)
 - Right click -> copy -> copy cURL
 - paste and send in insomnia
 - right click request on the left 

PURPOSE:
-To gather this week's list of best batters
REQUIREMENTS:
-requests, pandas
'''
# Imports----------------------------------------------------------------------
import requests
import pandas
from datetime import datetime
# Local Dependencies-----------------------------------------------------------
from skunkpack import logger
from skunkpack import datestrings

# Main-------------------------------------------------------------------------
def request_top_hitters(top_n=25, daysBack=-365, season=datetime.now().year):
    url = "https://bdfed.stitch.mlbinfra.com/bdfed/stats/player"
    payload = ""
    querystring = {"stitch_env":"prod","season":f"{season}","sportId":"1", \
                "stats":"season","group":"hitting","gameType":"R", \
                "limit":f"{top_n}","offset":"0","sortStat":"onBasePlusSlugging", \
                "order":"desc","daysBack":f"{daysBack}"
            }
    logger.log.debug(f'top_25_hitters request was made to mlbinfra.com')
    response = requests.request("GET", url, data=payload, params=querystring)
    data = response.json()
    stats = data['stats']
    df = pandas.json_normalize(stats)
    return df

if __name__ == '__main__':
    df = request_top_hitters()
    df.to_csv(f'__data\\Top_25_Hitters\\top_25_hitters_as_of_{datestrings.todays_date}.csv', index=False)
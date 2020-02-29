#! python3
# getWeather.py - Checks BBC Weather for a given postcode
import re
from requests_html import HTMLSession
session = HTMLSession()
# Get postcode 
yourLoc = input("Enter your postcode:")
# Shorten postcode for BBC weather
bbcLoc = re.compile(r"""
    ^(\w\w\w(\w)?)
    ([ ])?
    (\w\w\w)?$
    """, re.VERBOSE)
mo = bbcLoc.search(yourLoc)
postcode1 = mo.group(1).casefold()
# Check weather forecast
url = 'https://www.bbc.co.uk/weather/' + postcode1
print(f'Searching for weather in {postcode1.upper()} via {url}')
r = session.get(url)
r.html.render(sleep=0)
weather = '#wr-o-tabset__panel--today > div > div > p'
# Print weather forecast for today
try: 
    print(f'Weather for {postcode1.upper()}: {r.html.find(weather, first = True).text}')
except: 
    print('Sorry, couldn\'t find that location!')
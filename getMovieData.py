#! python3
# getOpenWeather.py – Gets the weather for any city using city name and country using an API

import json, requests, sys, logging
from keys import *
from pprint import pprint


logging.basicConfig(level=logging.WARNING, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable()
logging.debug('Start of program')

# Get location from command line args
if len (sys.argv) < 2:
	print('Usage: [TMDB id]')
	sys.exit()

TMDB_ID = ''.join(sys.argv[1])


# Download the JSON data from Openweathermp.org API
url = f'https://api.themoviedb.org/3/movie/{TMDB_ID}?api_key={TMDB_API_KEY}&language=en-US'
logging.debug(f'URL: {url}')


response = requests.get(url)
response.raise_for_status()

logging.debug(f'TMDB RESPONSE TEXT: {response.text}')

# load JSON into python dictionary:

movieData = json.loads(response.text)

print(f"{movieData['title']} ({movieData['release_date'][0:4]}): ", end='')
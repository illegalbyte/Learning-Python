#! python3
# searchpypi.py  - Opens several search results.

import requests
import sys
import webbrowser
import bs4
print('Searching...')    # display text while downloading the search result page
res = requests.get('https://pypi.org/search/?q='
                   + ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')


# TODO: Open a browser tab for each result.
linkElems = soup.select('.package-snippet')
for link in linkElems:
	urlToOpen = 'https://pypi.org' + link.get('href')
	print('Opening ', urlToOpen)
	webbrowser.open(urlToOpen)
	
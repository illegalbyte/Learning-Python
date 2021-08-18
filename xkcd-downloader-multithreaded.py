#! python3
# xkcd-downloader.py – downloads all XKCD comics automatically using Python webscraping.

import requests, os, bs4, threading

url = 'https://xkcd.com/'

# store in ./xkcd
os.makedirs('xkcd', exist_ok=True)

def downloadXkcd(startComic, endComic):
	global url
	for urlNumber in range(startComic, endComic):	
		# Download the page
		print(f'Downloading page {urlNumber}...')
		req = requests.get(f'{url}{urlNumber}')
		req.raise_for_status()
		xkcdHTML = bs4.BeautifulSoup(req.text, 'html.parser')


		# Find the URL of the comic image
		comicURL = 'https:' + xkcdHTML.select('#comic img')[0].get('src')

		# Download the comic image
		print(f'Downloading image {comicURL}...')
		req = requests.get(comicURL)
		req.raise_for_status()

		# Save the image to ./xkcd
		imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')

		for chunk in req.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()
		'''		
		# Get the prev button's url 
		prevLink = xkcdHTML.select(
			'#middleContainer > ul:nth-child(4) > li:nth-child(2) > a')[0]
		url = 'https://xkcd.com' + prevLink.get('href')
		'''

# start multithreading

downloadThreads = []
for i in range(0, 140, 10):
	start = i 
	end = i + 9
	if start == 0:
		start = 1
	downloadThread = threading.Thread(target=downloadXkcd, args=(start,end))
	downloadThreads.append(downloadThread)
	downloadThread.start()

for downloadThread in downloadThreads:
	downloadThread.join()

print('Done')

#! python3
# xkcd-downloader.py – downloads all XKCD comics automatically using Python webscraping.

import requests, os, bs4

url = 'https://xkcd.com'

os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
	# Download the page
	print('Downloading page %s...' % url)
	req = requests.get(url)
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

	# Get the prev button's url 
	prevLink = xkcdHTML.select(
		'#middleContainer > ul:nth-child(4) > li:nth-child(2) > a')[0]
	url = 'https://xkcd.com' + prevLink.get('href')



print('Done')

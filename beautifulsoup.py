#! python3

import requests, bs4

res = requests.get('https://nostarch.com')
res.raise_for_status() 

noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

bookName = noStarchSoup.select('div.field.field-name-body.field-type-text-with-summary.field-label-hidden > div > div > p > a')
print(bookName)

for book in bookName:
	print(book.getText())
	print(book.get('href'))
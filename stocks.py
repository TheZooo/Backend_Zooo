import bs4
import requests

# Makes a request, "res", for stock market watcher and checks status
res = requests.get('https://www.marketwatch.com/investing/stock/0006')
res.raise_for_status()

# Calling a function to pull the text in res parsing with lxml
goog = bs4.BeautifulSoup(res.text, features="lxml")

# Prints out all the texts in elements with 'bg-quote[field="change"]'
elems = goog.select('bg-quote[field="change"]')
#for x in elems:
#	print(x.getText())
	
# Selecting index 0 in elems and getting it's innerHTML
price = elems[0].getText()

# Replacing commas with periods
priceNoDec = price.replace(',','.')
print(priceNoDec)

finalPriceFloat = round(float(priceNoDec), 0)
print(int(finalPriceFloat))

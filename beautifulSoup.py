import bs4, requests

def getPrice(url):
	res=requests.get(url);
	res.raise_for_status();
	soup=bs4.BeautifulSoup(res.text,'html.parser')
	elems=soup.select('#mediaNoAccordion > div.a-row > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')
	return elems[0].text.strip();

price=getPrice('http://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/')
print('Price is :' +str(price))
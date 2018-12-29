from bs4 import BeautifulSoap as soup
from urllib.request import urlopen as uReq

url = 'https://www.nyse.com/quote/XNYS/'

text = input().trim()
query = text.split(':')[0]

uClient = uReq(url+query)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

container = page_soup.match("div", {"class":"d-dquote-bigContainer"})

company_name = container.match("div",{"class": "d-dquote-bigContainer"})
last_trade_time = container.match("div",{"class":"d-dquote-time"})

print('Comapany Name: '+ company_name)
print('Last Trade Time: '+ last_trade_time)

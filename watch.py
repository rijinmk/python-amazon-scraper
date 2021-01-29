import requests
import urllib2
import time
import bs4

url = "https://www.amazon.ae/gp/product/B08HHFL27C"


while True: 
    page = requests.get(url)
    html = page.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    print(soup.find("span", {"id" : "priceblock_ourprice"}).text + " " +  soup.find("div", {"id" : "availability"}).text)
    time.sleep(10)
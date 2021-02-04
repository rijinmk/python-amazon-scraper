import requests
import urllib2
import time
import bs4
from datetime import datetime
import sys
import os
import json

url = "https://www.amazon.ae/s?k=ps5&ref=nb_sb_noss_1"
scraped_data = {}

while True: 
    page = requests.get(url)
    html = page.text
    soup = bs4.BeautifulSoup(html, "html.parser")

    #Each result
    results = soup.findAll("div", {"class": "s-result-item"})
    scraped_each = []
    for i in range(len(results)): 
        price = results[i].find("span", {"class": "a-price-whole"})
        if(price):
            price = int(price.text.replace(".","").replace(",",""))
            if(price > 1900):
                name = results[i].find("span", {"class": "a-text-normal"}).text.encode("utf-8")
                link = "https://www.amazon.ae" + results[i].find("a", {"class": "a-link-normal"})["href"].encode("utf-8")
                reviews = results[i].select_one(".a-link-normal span.a-size-base").text.encode("utf-8")
                star = results[i].select_one(".a-icon-star-small .a-icon-alt").text.encode("utf-8")
                image = results[i].select_one(".s-image-square-aspect img")["src"].encode("utf-8")
                jsonify = {"name": name,"link": link,"reviews": reviews,"star": star,"image": image, "price": price}
                scraped_each.append(jsonify)

    f = open("view/scrapred_results.json", "rb")
    d = f.read()
    f.close()

    if(len(scraped_each) > 0):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time())))
        d = json.loads(d)
        d[time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))] = scraped_each
        d = json.dumps(d)

        f = open("view/scrapred_results.json", "wb")
        d = f.write(d)
        f.close()

    time.sleep(60 * 10)
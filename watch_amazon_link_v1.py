'''
Version: 0.0.1
Description: 
Done: 
- One specific link
- Keeps a track of the stock and price
- Logs time also
Todo: 
- Add sound OR send email when price is below 2500
'''

import requests
import time
import bs4
from datetime import datetime
import sys
import os
try: 
    import winsound
except: 
    pass

url = "https://www.amazon.ae/gp/product/B08HHFL27C"

def playASound():
    if sys.platform == "win32":
        winsound.PlaySound("*", winsound.SND_ALIAS)
    elif sys.platform == "darwin":
        os.system('say Oh my god buy now')

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}

while True: 
    page = requests.get(url, headers=headers)
    print(page)
    html = page.text
    soup = bs4.BeautifulSoup(html, 'html.parser').encode('utf-8')

    #testing
    f = open('ps5.html', 'wb')
    f.write(soup)
    f.close()
    break

    # Extract information
    price = float(soup.find("span", {"id" : "priceblock_ourprice"}).text.replace(u'\xa0', u' ').split(' ')[1].replace(u',', u''))
    stock = soup.find("div", {"id" : "availability"}).text.strip()

    # Time
    now = datetime.now()
    current_time = now.strftime("%D - %H:%M:%S")

    if(price < 2500):
        # playASound()
        print("BUY NOW: ")
    else: 
        print("Don't buy: ")

    print(current_time, price, stock)
    
    time.sleep(60 * 5)



    
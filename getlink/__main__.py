import sys
import random
import bs4 as bs
import time
import requests
import firebase_admin
import datetime
from firebase_admin import credentials
from firebase_admin import db
from datetime import date

def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # get the HTTP response and construct soup object
    soup = bs.BeautifulSoup(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:    
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    # print(proxies)
    return proxies

def scrape(dict):
    start = time.time()
    proxylist = get_free_proxies()
    result = "Success"
    #connect to firebase
    cred = credentials.Certificate({
    })
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://airdna-3d619-default-rtdb.firebaseio.com/'
    })
    ref = db.reference('/properties/')
    print("conntected to firebase")
    if 'link' in dict:
        link = dict['link']
        # link = "/1688590?unitId=2250051&noDates=true"
        
        # parse link
        pid = link[link.find("unitId=")+7:link.find("&")]
        print("------------------------------------------------------")
        print(pid)
        print(link)

        # make curl requests- collect web info
        print("Now checking pid #", pid)
            # make curl requests- collect web info
        pcheck=0
        try:
            while(pcheck < 10) :
                proxy = random.choice(proxylist)
                try:
                    response = requests.get(f'https://www.vrbo.com{link}', timeout=10)
                    print("proxy worked")
                    break
                except:
                    print("proxy didn't work. checking another proxy.")
        except:
            pass

        # retrieve site contents
        text = response.text
        soup = bs.BeautifulSoup(text, 'html.parser')
        # print(soup)

        # scrape price info
        price = soup.find("meta",  property="og:price:amount", content=True)
        if price:
            print("price: "+price["content"])
            box_ref = ref.child(pid)
            box_ref.update({'price':price["content"]})
        else:
            result = 'price not found'
            print("price not found")
         # scrape rating info
        rating = soup.find("meta",  property="og:rating", content=True)
        if rating:
            print("rating: "+rating["content"])
            box_ref = ref.child(pid)
            box_ref.update({'rating':rating["content"]})
        else:
            result = 'rating not found'
            print("rating not found")
        currency = soup.find("meta",  property="og:price:currency", content=True)
        if currency:
            print("currency: "+currency["content"])
            box_ref = ref.child(pid)
            box_ref.update({'currency':currency["content"]})
        else:
            result = 'currency not found'
            print("currency not found")
        siteName = soup.find("meta",  property="og:site_name", content=True)
        if siteName:
            print("siteName: "+siteName["content"])
            box_ref = ref.child(pid)
            box_ref.update({'siteName':siteName["content"]})
        else:
            result = 'siteName not found'
            print("siteName not found")
        description = soup.find("meta",  property="og:description", content=True)
        if description:
            print("description: "+description["content"])
            box_ref = ref.child(pid)
            box_ref.update({'description':description["content"]})
        else:
            result = 'description not found'
            print("description not found")
        location = soup.find("div", {"class": "Description--location"})
        if location:
            print("location: "+location.text)
            locationlist = (location.text).split(", ")
            box_ref = ref.child(pid)
            box_ref.update({'location':location.text})
            box_ref.update({'city':locationlist[0]})
            box_ref.update({'state':locationlist[1]})
            box_ref.update({'country':locationlist[2]})
        else:
            result = 'location not found'
            print("location not found")
        # ct stores current time
        today = date.today()
        # dd/mm/YY
        d1 = today.strftime("%d/%m/%Y")
        if d1:
            print("current time:-", d1)
            box_ref = ref.child(pid)
            box_ref.update({'current time':d1})

    else:
        result = 'link is required'
        print(result)
    end = time.time()
    print(end - start)
    return {'result':result,'time': (end - start)}
 
def main():
 return scrape("sys.args")
 
if __name__ == "__main__":
    main()
import sys
import random
import bs4 as bs
import time
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

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
    print(proxies)
    return proxies

def scrape(dict):
    start = time.time()
    proxylist = get_free_proxies()
    #connect to firebase
    ref = db.reference('/')
    print("conntected to firebase")
    if 1:
        link = "/1688590?unitId=2250051&noDates=true"
        # link = dict['link']
        
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
                    response = requests.get(f'https://www.vrbo.com{link}', timeout=10,proxies={"http":proxy, "https":proxy})
                    print("proxy worked")
                    break
                except:
                    print("proxy didn't work. checking another proxy.")
        except:
            pass

        # retrieve site contents
        text = response.text
        soup = bs.BeautifulSoup(text, 'html.parser')

        # scrape price info
        price = soup.find("meta",  property="og:price:amount", content=True)
        if price:
            print(price["content"])
            box_ref = ref.child(pid)
            box_ref.update({'price':price["content"]})
        else:
            result = 'price not found'
            print("price not found")

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
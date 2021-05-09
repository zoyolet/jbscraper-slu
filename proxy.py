#!/usr/bin/env python3

import random
import sys
import requests
import bs4 as bs


def get_free_proxies(params):
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
    print(random.choice(proxies))
    return proxies
    
def main():
    return get_free_proxies("test")
 
if __name__ == "__main__":
    main()
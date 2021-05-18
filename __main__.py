from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import re
import os
import csv
import requests
import time
import bs4 as bs
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random
import simplejson as json

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

def scrape(params):
    start = time.time()
    loop = 1
    linklist = []
    # get Link 
    while loop<=1:
        url = 'https://www.vrbo.com/search/keywords:galveston-texas-united-states-of-america/page:'+str(loop)
        browser = webdriver.Remote("http://ec2-18-232-186-5.compute-1.amazonaws.com:4444/wd/hub", DesiredCapabilities.CHROME)
        browser.get(url)
        y = 1000
        print("enter the website")
        time.sleep(2) # load the page
        for timer in range(0,50):
            browser.execute_script("window.scrollTo(0, "+str(y)+")")
            y += 1000  
            time.sleep(1)
        time.sleep(1)
        html = browser.page_source
        soup = bs.BeautifulSoup(html,'html.parser')
        for tag in soup.find_all("a", href=True):
            if "unitId" in tag["href"]:
                linklist.append(tag["href"]) 
        loop+=1
    for link in linklist:
        # parse link
        url = "https://us-south.functions.cloud.ibm.com/api/v1/namespaces/kitchana.thamutok%40slu.edu_replica-airdna/actions/getinformationBylink7?blocking=true"
        data = {'link': link}
        headers = {'Content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(data), headers=headers, auth=())
       
    end = time.time()
    print(end - start)
    return {'result': 'success!'}

def main():
 return scrape("sys.args")
 
if __name__ == "__main__":
    main()




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
    proxylist = get_free_proxies()
    #connect to firebase
    cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "airdna-3d619",
  "private_key_id": "35876803cfa5e4916570b39257f05b6eea2cd40f",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDEaZ2CWOWJtLWB\n1G0zF4KSM0pU/2m+WWRk8vgPlNrB2K/iBaVP1mQsaccEcfeHthsyH7+mqOKXMACa\npPjqKiKEVJQGdjRZlV8lODQfmG061umNNi5rZQalWSjC2J4OXfc2Oh1y2npI7JL+\nR50c5qDM/JnyUOW2uDGIqmQO633Ybm+h/5eWmZjcXdrqqLI3Ef8XClVGqK4lXhF3\ntcpM8XxTYlLG83HmeFxP/hgQqZfVEh2KaHwxdkKjL9JXUUlmV4wi7cjL2EmumjlG\n11irAOIjqhLLMY8Nb48BTcyckmbIYNgwf3wOoVK2jteKZ5jnGb85k0qY6g7bo9tz\nY99GYTixAgMBAAECggEAEVsw4T4YSIcou+iI3skuz1sLcD/iuQCeu8HxtDTH8PXE\nMxGjJk8wanFNdiHZCQvJUvBVx/UoEsqZ3xCBc3XWN4He08RZw2nM7tXM21blnhu0\nJzeYugJDKFTc4nzwWJ4qlIblp8rRIAURxzkOU+m4X2zZ8Lz/05nqvKQr89qQ9BFE\nSzQqLmWWvoPmjvEj3ho953Oa2RE37lDTtWGBv/arlEuwLHr1jyFny10HEveEOztV\nsmSaiZ5NJ8KbK4EcTefJWXa5gjkOTIKSFD2Emfk9/vVKD8riyhpmbga/Q6o0NRsY\nM9gL4ImGxt1aaiptEQv37Oa48Hmp6gblqbAHGczBLQKBgQD9oEt1TKWxidcdoUdc\nl5FV8aCODT1LiIRdeWaZBXgqpjNqVO6BkXK0EpmA65gsXU/Vd6r5+Hng6yP0s/Ve\nQO08Sn/plyoVlwH//Wt0U3BLTnnDTvXoLcysE5gr2aI7eF7gu/2M26Sab1cQgV6n\nOL9HoxfgNVe7+D2Djz3pI+UCtQKBgQDGQDugTW7Xaken+dYWWC9EyDUViUWtwlA/\nbXxJVsAIkxoLdYRB5Y/MyP+9hpRVhTG2puxHvbp4uYbVxp83rLi7DXuFc1wafqnY\nr5tw5u1jF+zR+USiACEcfHi2U3/toiYLyr1hO3qOdybsVQTHT+iej1j55syq73nZ\n7ShYyPGvjQKBgBhAytZ1tOaMUtjPgl51U/2O9JaA55qgfF/f6xK49ivF5ubFJmWX\nfguAN9OfM9cSOT8liWEMBMOgWLjeuJkBxm3chezVer3DyforxqnCDNv2rigiFdvU\n/Vx7JzMSRbRAJ3qAH5fnrQ7jlMTMSjvdblUwYGkdUL112JQLD5WKzCx9AoGAXp9p\n1ikfLlHbwaDNPfz5Eqs8KvtJ9pU4GA35tEdjgLQ1SiLc7VbUO7nz1lHVmrvn7nXd\ncKBt0BE8+evDMp+NzDmzKw7UdxDdoD6wwkJ2K0XQEqgWyful0iLWuq8/7/vkjNxH\nZ5Er/bOBMGujzD2nmYZxwVUXer6yOgGnsDi4okECgYEAx5axIECVcV8osLirRoIb\n7GHs7PuwnIDpDt/OICd7Xeju0zGno6zs72P4Nd5cOBiHfpGp+4Bm3xSLOM3tEfFz\na5/meS9XRDKMamQ4q4Kgew9syPxc875uXeVEkH5SGfWl3qZ3y+6E5HoTgSt0UAtk\nwb0/GqMLYSkqjDFTU660FXo=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-8a1s0@airdna-3d619.iam.gserviceaccount.com",
  "client_id": "111546907438034843549",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-8a1s0%40airdna-3d619.iam.gserviceaccount.com"
})
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://airdna-3d619-default-rtdb.firebaseio.com/'
    })
    ref = db.reference('/')
    print("conntected to firebase")
    loop = 1
    linklist = []
    # get Link 
    while loop<=1:
        url = 'https://www.vrbo.com/search/keywords:missouri-united-states-of-america/page:'+str(loop)
        browser = webdriver.Remote("http://ec2-44-192-45-45.compute-1.amazonaws.com:4444/wd/hub", DesiredCapabilities.CHROME)
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
            print("price not found")
    end = time.time()
    print(end - start)
    return {'Data': 'Saved!'}

def main():
 return scrape("sys.args")
 
if __name__ == "__main__":
    main()




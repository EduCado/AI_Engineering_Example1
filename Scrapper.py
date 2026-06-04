from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

def getlinks1(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    #title = soup.title.text
    #links = soup.find_all("a")
    links = [
    a.get("href")
    for a in soup.find_all("a")
    if a.get("href")
    ]

    return links


#links=getlinks1("https://community.uipath.com/")
#print(links)
#for link in links:
   #print("Link:", link.get("href"))

#print("Number of links:", len(links))
#print("Title:", title)

def getlinks(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    links = []

    for a in soup.find_all("a", href=True):
        href = urljoin(url, a["href"])  # convert relative to absolute

        if href.startswith(("http://", "https://")):
            links.append(href)

    return list(set(links))  # remove duplicates


links = getlinks("https://community.uipath.com/")
print(links)



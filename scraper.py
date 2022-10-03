# from django.http import response
from os import link
import requests 
from bs4 import BeautifulSoup
import random

def scrape_wiki_article(url):
    response = requests.get(
    url = url,
    )

    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find(id="firstHeading")
    print(title.string)

    # get all the links 

    allLinks = soup.find(id = "bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks: 
        if link['href'].find('/wiki/') == -1:
            continue
        linkToScrape = link
        break

    scrape_wiki_article("https://en.wikipedia.org" + linkToScrape['href'])




scrape_wiki_article("https://en.wikipedia.org/wiki/Web_scraping")








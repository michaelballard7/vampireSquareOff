import requests
from bs4 import BeautifulSoup as bs


class Scraper():
    
    def __init__(self):
            counter = 0
            self.url = "https://en.wikipedia.org/wiki/List_of_vampire_traits_in_folklore_and_fiction"

    def fetcher(self):
        response = requests.get(self.url)
        print(response.status_code)
        html = response.text.strip()
        return html

    def get_url(self):
        url = self.url
        return url

    def processer(self):
        html =  self.fetcher()
        soup = bs(html, 'lxml')
        title = soup.title.text.strip()
        return title

    def formatter():
        pass






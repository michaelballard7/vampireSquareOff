import requests
from bs4 import BeautifulSoup as bs


class Scraper():
    
    def __init__(self):
            counter = 0
            self.url = "https://en.wikipedia.org/wiki/List_of_vampire_traits_in_folklore_and_fiction"

    def fetcher(self):
        response = requests.get(self.url)
        html = response.text.strip()
        return html

    def get_url(self):
        url = self.url
        return url

    def processer(self):
        html =  self.fetcher()
        soup = bs(html, 'lxml')
        title = soup.title.text.strip()
        table = soup.table
        table_row= table.findAll("tr")
        fav_vampires = []
        titles = ["Blood Lad","Monster High","The Mortal Instruments","Vampire in Brooklyn"]
        for title in titles:
            if table.find("a", {"title": title}):
                fav_vampires.append(title)
        return {"title":title,"faves":fav_vampires}

    def formatter():
        pass


vampire_list = Scraper()

print(vampire_list.processer())



import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def is_external_link(base_url, link):
    base_domain = urlparse(base_url).netloc
    link_domain = urlparse(link).netloc
    return base_domain != link_domain


class Scrapper:
    def __init__(self, url):
        self.url = url
        self.title = None
        self.headers = None
        self.text = None
        self.links = None

    def Scrape(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")

        self.title = soup.title.string
        self.headers = [
            h.get_text()
            for h in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
            if h.get_text() != ""
        ]
        self.text = [p.get_text() for p in soup.find_all("p") if p.get_text() != ""]
        self.links = [
            urljoin(self.url, link.get("href"))
            for link in soup.find_all("a")
            if link.get("href") is not None
            and is_external_link(self.url, urljoin(self.url, link.get("href")))
        ]

        # print('Title:', self.title)
        # print('Headers:', self.headers)
        # print('Text:', self.text)
        # print('Links:', self.links)

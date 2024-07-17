import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re


class Scrapper:
    def __init__(self, url):
        self.url = url
        self.title = ""
        self.content = ""
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

    def Scrape(self):
        try:
            headers = {"user_agent": self.user_agent}
            response = requests.get(self.url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")

            self.title = soup.title.string if soup.title else ""
            self.content += self.CleanText(self.title) + "\n\n"

            for header in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
                self.content += self.CleanText(header.text) + "\n"

            for paragraph in soup.find_all("p"):
                self.content += self.CleanText(paragraph.text) + "\n"

            time.sleep(1)

            self.content = self.CleanText(self.content)

            print(self.content)
        except requests.exceptions.RequestException as e:
            print(f"Error scraping URL: {e}")

    def CleanText(self, text):
        text = re.sub(r"\s+", " ", text).strip()
        # polish letters
        text = re.sub(r"[^a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ\s./!?]", " ", text)
        return text

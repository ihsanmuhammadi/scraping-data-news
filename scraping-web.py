from bs4 import BeautifulSoup
import requests

def scrape_news():
    url = "https://os.cuydrone.id"
    response = requests.get(url)
    element = BeautifulSoup(response.content, "html.parser")
    headline = element.find("div", class_="headline")
    print(headline.text)

scrape_news()
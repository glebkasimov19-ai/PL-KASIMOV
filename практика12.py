import requests
from bs4 import BeautifulSoup
import json

url = "https://habr.com/ru/post/453440/"

response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")

#извлечение
article = {
    "title": soup.find("meta", property="og:title")["content"] if soup.find("meta", property="og:title") else "",
    "views": soup.find("span", class_="tm-icon-counter__value").text.strip() if soup.find("span", class_="tm-icon-counter__value") else "",
    "description": soup.find("meta", property="og:description")["content"] if soup.find("meta", property="og:description") else "",
    "url": soup.find("meta", property="og:url")["content"] if soup.find("meta", property="og:url") else "",
    "images": [img["content"] for img in soup.find_all("meta", property="og:image")]
}

#сохранение в json
with open("habr_article.json", "w", encoding="utf-8") as f:
    json.dump(article, f, ensure_ascii=False, indent=4)

print("Основная информация сохранена в habr_article.json")


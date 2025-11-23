import requests
from bs4 import BeautifulSoup
import json

url = "https://habr.com/ru/post/453440/"

response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")

# Извлекаем данные
article = {
    "title": soup.find("meta", property="og:title")["content"] if soup.find("meta", property="og:title") else "",
    "date": soup.find("meta", property="article:published_time")["content"] if soup.find("meta", property="article:published_time") else "",
    "description": soup.find("meta", property="og:description")["content"] if soup.find("meta", property="og:description") else "",
    "url": soup.find("meta", property="og:url")["content"] if soup.find("meta", property="og:url") else "",
    "images": [img["content"] for img in soup.find_all("meta", property="og:image")]
}

# Сохраняем результат в JSON
with open("habr_article.json", "w", encoding="utf-8") as f:
    json.dump(article, f, ensure_ascii=False, indent=4)

print("Основная информация сохранена в habr_article.json")


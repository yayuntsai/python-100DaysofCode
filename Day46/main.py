from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     contents = file.read()

enter_date = input("Which year do you want to travel to?(Format: YYYY-MM-DD)")

url = f"https://www.billboard.com/charts/hot-100/{enter_date}"
response = requests.get(url)
html_doc = response.text




soup = BeautifulSoup(html_doc, "html.parser")
articles = soup.find_all("span", "chart-element__information__song")

article_texts = []

for article in articles:
    text = article.get_text()
    article_texts.append(text)

print(article_texts)
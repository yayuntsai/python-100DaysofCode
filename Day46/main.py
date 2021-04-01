from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     contents = file.read()

url = "https://www.billboard.com/charts/hot-100/2021-04-01"
response = requests.get(url)
html_doc = response.text


soup = BeautifulSoup(html_doc, "html.parser")
print(soup)
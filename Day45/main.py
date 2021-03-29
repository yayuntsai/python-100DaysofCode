from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     contents = file.read()

url = "https://news.ycombinator.com"
response = requests.get(url)
html_doc = response.text
#print(html_doc)

soup = BeautifulSoup(html_doc, "html.parser")
articles = soup.find_all("a","storylink")
# print(article_tag.get_text())
article_texts = []
article_links = []

for article_tag in articles:
    article_link = article_tag["href"]
    article_links.append(article_link)
    texts = article_tag.get_text()
    article_texts.append(texts)
print(article_link, article_texts)

article_upvote = soup.find("span", "score").get_text()
# print(article_upvote)
#
#
# # 一些屬性或方法
# print(soup.title) # 把 tag 抓出來
# print("---")
# print(soup.title.name) # 把 title 的 tag 名稱抓出來
# print("---")
# print(soup.title.string) # 把 title tag 的內容抓出來
# print("---")
# print(soup.title.parent.name) # title tag 的上一層 tag
# print("---")
# print(soup.a) # 把第一個 <a></a> 抓出來
# print("---")
# print(soup.find_all('a')) # 把所有的 <a></a> 抓出來
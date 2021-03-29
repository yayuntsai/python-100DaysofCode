from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     contents = file.read()

url = "https://news.ycombinator.com"
response = requests.get(url)
html_doc = response.text

soup = BeautifulSoup(html_doc, "html.parser")
# 一些屬性或方法
print(soup.title) # 把 tag 抓出來
print("---")
print(soup.title.name) # 把 title 的 tag 名稱抓出來
print("---")
print(soup.title.string) # 把 title tag 的內容抓出來
print("---")
print(soup.title.parent.name) # title tag 的上一層 tag
print("---")
print(soup.a) # 把第一個 <a></a> 抓出來
print("---")
print(soup.find_all('a')) # 把所有的 <a></a> 抓出來
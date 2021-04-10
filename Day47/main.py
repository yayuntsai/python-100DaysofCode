from bs4 import BeautifulSoup
import requests
import lxml



url = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
                                     "Accept-Language": "zh-tw"})
response.raise_for_status()
html_doc = response.text


soup = BeautifulSoup(html_doc, "lxml")
price = soup.find("span", "a-size-medium a-color-price").get_text()
print(price)

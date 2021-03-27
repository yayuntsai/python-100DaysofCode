import requests
import json
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "AC395eba2befd04b8488ebaec1950fd970"
auth_token = "c9534fb451ce30aca775b6290f797490"
API_KEY = "NNX2PXUTI0HTXYNP"

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.
#Call API and get row data
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()
every_record = stock_data["Time Series (Daily)"]
#Put everyday data in a list
every_record_list = [value for (key, value) in every_record.items()]


close_data_list = []
for record in every_record_list:
    close_data = record["4. close"]
    close_data_list.append(close_data)

n = 1
for record in close_data_list:
    if n < len(close_data_list):
        vary_rate = (float(close_data_list[n-1])-float(close_data_list[n])) / float(close_data_list[n])
        # print(vary_rate)
        if vary_rate > 0.05 or vary_rate < -0.05:
            ## STEP 2: Use https://newsapi.org/docs/endpoints/everything
            # Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
            # HINT 1: Think about using the Python Slice Operator
            news_api_key = "ae90fb4499b04843ac044632a768b595"
            news_params = {
                "q": COMPANY_NAME,
                "from": "2021-03-26",
                "to": "2021-03-26",
                "sortBy": "popularity",
                "apiKey": news_api_key
            }
            response = requests.get(NEWS_ENDPOINT, params=news_params)
            response.raise_for_status()
            articles = response.json()['articles']
            three_articles = articles[:3]

            ## STEP 3: Use twilio.com/docs/sms/quickstart/python
            # Send a separate message with each article's title and description to your phone number.
            # HINT 1: Consider using a List Comprehension.
            formatted_articles = [f"Title: {article['title']}. \nDescription: {article['description']}" for article in three_articles]
            client = Client(account_sid, auth_token)

            for article in formatted_articles:
                message = client.messages \
                    .create(
                    body = article,
                    from_ = '+16092706262',
                    to='+886937485999'
                )
            print(message.status)
        n += 1



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


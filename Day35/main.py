import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_LEY")
account_sid = "AC395eba2befd04b8488ebaec1950fd970"
auth_token = os.environ.get("AUTH_TOKEN")


weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "exclude": "current, minutely, hourly"
}


response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()


hourly_data_list = weather_data['hourly'][:12]
will_rain = False

#weather_id = hourly_data_list[0]['weather'][0]['id'] # figure the weather id in the JSON
for weather_data in hourly_data_list:
    condition_code = weather_data['weather'][0]['id']
    if condition_code < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ.get("https_proxy")}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
            body="It's going to rain. Bring an umbrella",
            from_='+16092706262',
            to='+886937485999'
        )
    print(message.status)
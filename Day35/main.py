import requests
import os
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "526feb582389c4857fc9dd763b456bbc"
account_sid = "AC395eba2befd04b8488ebaec1950fd970"
auth_token = "443108b381ba9a92bb746767f2803c03"
client = Client(account_sid, auth_token)

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
    message = client.messages \
        .create(
            body="It's going to rain. Bring an umbrella",
            from_='+16092706262',
            to='+886937485999'
        )
    print(message.status)
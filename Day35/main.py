import requests

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "526feb582389c4857fc9dd763b456bbc"
weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
}


response = requests.get(OWM_endpoint, params=weather_params)
print(response.json())
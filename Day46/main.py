from bs4 import BeautifulSoup
import requests
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

# with open("website.html") as file:
#     contents = file.read()
CLIENT_ID = "d904616d0451406b9267cc19c9c7747b"
CLIENT_SECRET = "9e115fb01a554a87bf7162be3d859b6d"
OAUTH_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"

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



# Call Spotify API
spotify_params = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "redirect_uri": "http://example.com",
    "scope": "user-library-read"
}

auth_manager = SpotifyOAuth(client_id="d904616d0451406b9267cc19c9c7747b",
    client_secret="9e115fb01a554a87bf7162be3d859b6d",
    redirect_uri="http://example.com",
    scope="playlist-modify-private",
    cache_path="token.txt",
    username="anniesnoopymd@yahoo.com.tw")
sp = spotipy.Spotify(auth_manager=auth_manager)
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
#
# ))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
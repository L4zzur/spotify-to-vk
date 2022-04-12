import vk_api
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from config import TOKEN, client_id, client_secret, redirect_uri, username, scope, status

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        username=username,
        scope=scope,
    ),
    language='ru'
)

session = vk_api.VkApi(token=TOKEN)
vk = session.get_api()

def set_user_status(text):
    vk.status.set(text=text)

def update_status():
    global last_status
    current = spotify.current_user_playing_track()
    if current is None or not current['is_playing']:
        if last_status != status:
            print("None")
            last_status = status
            set_user_status(status)
    else:
        track = current["item"]["name"]
        album = current["item"]["album"]["name"]
        artist = current["item"]["artists"][0]["name"]
        music = 'Spotify | ' + artist + ' - ' + track + ' - ' + album
        if len(music) > 140:
            music = music[:139][:music.rfind(' ')] + '…'
        if last_status != music:
            last_status = music
            print(music)
            set_user_status(music)

if __name__ == '__main__':
    last_status = None
    while True:
        try:
            update_status()
        except Exception as e:
            print(f'Произошла ошибка: {e}')
        time.sleep(5)

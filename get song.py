import requests
import threading


def get_song():
    threading.Timer(5.0, get_song).start()

    file = open('D:\\Users\\Kristian\\Desktop\\song.txt', 'w', encoding='utf-8')

    header = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer BQBKOyWbFQLSk271Ri16EYTej7MfdctBc1ikzsgXG2aAhGuxFvglonI2IPVGxb6lG7sM0g1RvsSbSAWDgqA3mqIauJ3nwoKXjalMcC4u6SeCAudHJDvfuu2cy-zx55mFszsFl6wHOcNIrfX9ZuY',
    }
    response = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=header)
    response = response.json()
    artist = response['item']['artists'][0]['name']
    song = response['item']['name']

    file.write(f'{artist} - {song}  |  ')
    file.close()


if __name__ == '__main__':
    get_song()

import requests
import threading
import base64

client_id = '91c0cfc459bc441fb7debc5d72544eec'
client_secret = '19cd1e6522d4415e84ace6584db565bd'


def send_refresh():
    refresh_token = REFRESH_TOKEN_FROM_CURL
    grant_type = 'refresh_token'
    client_creds = f'{client_id}:{client_secret}'
    client_creds_b64 = base64.b64encode(client_creds.encode()).decode()
    token_url = 'https://accounts.spotify.com/api/token'
    token_data = {
        'grant_type': grant_type,
        'refresh_token': refresh_token
    }
    token_headers = {
        'Authorization': f'Basic {client_creds_b64}'
    }

    r = requests.post(url=token_url, data=token_data, headers=token_headers)
    r = r.json()
    token = r['access_token']

    return token


def get_song():
    threading.Timer(5.0, get_song).start()

    file = open(PATH_TO_OUTPUT_FILE, 'w', encoding='utf-8')
    global token

    auth = f'Bearer {token}'
    header = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': auth
    }
    response = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=header)
    
    response = response.json()
    try:
        artist = response['item']['artists'][0]['name']
        song = response['item']['name']
        file.write(f'{artist} - {song}  |  ')
    except:
        token = send_refresh()

    file.close()


if __name__ == '__main__':
    global token
    token = send_refresh()
    get_song()

    # client_creds = f'{client_id}:{client_secret}'
    # client_creds_b64 = base64.b64encode(client_creds.encode()).decode()
    # response_type = 'code'
    # redirect_uri = 'https%3A%2F%2Fexample.com%2Fcallback%2F'
    # scope = 'user-read-currently-playing'
    #
    # get_params = {
    #     'client_id': client_creds_b64,
    #     'response_type': response_type,
    #     'redirect_uri': redirect_uri,
    #     'scope': scope
    # }

    # auth_url = f'https://accounts.spotify.com/authorize?client_id={client_id}&response_type={response_type}&redirect_uri={redirect_uri}&scope={scope}'
    # webbrowser.open(auth_url, new=2)
    # code = input('Paste everything after \'code=\' here: ')
    # print(code)
    # print(client_creds_b64)
    # print(redirect_uri)
    # print(f'curl -H \"Authorization: Basic {client_creds_b64}\" -d grant_type=authorization_code -d code={code} -d redirect_uri={redirect_uri} https://accounts.spotify.com/api/token')

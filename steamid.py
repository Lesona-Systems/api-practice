import requests
import utilities as u

def main():
    url = _form_response_url()
    response = requests.get(url)
    response = response.json()
    user_steam_id = response['response']['steamid']
    print(f'SteamId: {user_steam_id}')

def _form_response_url():
    api_key = u.get_api_key()
    vanity_url = u.get_vanity_url()
    request_url = f"http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={api_key}&vanityurl={vanity_url}"
    return request_url

if __name__ == '__main__':
    main()
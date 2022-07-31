from configparser import ConfigParser
config = ConfigParser()

def get_api_key():
    config.read('secrets.ini')
    return config['steam']['api_key']

def get_token():
    config.read('secrets.ini')
    return config['steam']['oauth_token']

def get_vanity_url():
    return input('What is your Steam URL?: ')

if "__name__" == "__main__":
    main()
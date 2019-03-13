import os
import appdirs


def load_token():
    cwd = os.getcwd()
    token = os.environ.get('ENTSOE_API_TOKEN')
    # TODO: Consider https://github.com/theskumar/python-dotenv
    if not token and "entsoe_api_token.txt" in os.listdir(cwd):
        token = open("entsoe_api_token.txt").readlines()[0].strip()
    if not token:
        raise ValueError("Can't find ENTSO-E token")
    return token


TOKEN = load_token()
DATA_DIR = appdirs.user_data_dir("bonsai", "bentso")

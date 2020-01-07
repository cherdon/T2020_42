import os
import json
secrets_json = os.path.join(os.path.dirname(__file__), 'secrets.json')
with open(secrets_json, 'r') as infile:
    secrets = json.load(infile)


class Config(object):
    SECRET_KEY = "1234"
    API_VERSION = "v1.0"

    HOST = "0.0.0.0"
    PORT = 80
    DEBUG = True

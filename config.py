import os


class Config(object):
    HOST = "0.0.0.0"
    PORT = 80
    SECRET_KEY = '1234'

    ENV = 'development'
    DEBUG = True

    TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), 'frontend', 'src', 'pages')
    STATIC_PATH = os.path.join(os.path.dirname(__file__), 'frontend', 'src', 'images')

    API_URL = "https://techtrek.herokuapp.com/api/v1.0"
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.template_folder = app.config['TEMPLATES_PATH']
app.static_folder = app.config['STATIC_PATH']

from app import routes


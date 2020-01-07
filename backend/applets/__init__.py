import json
import datetime
from bson.objectid import ObjectId
from flask import Flask
from flask_restful import Api
from backend.config import Config


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)


app = Flask(__name__)
app.config.from_object(Config)
app.json_encoder = JSONEncoder
api = Api(app)

# To set up API endpoints, simply import the class(Resource) and put the following:
# api.add_resource(class, '/api/v1.0/SOMETHING')

from backend.applets.app1 import SomethingAPI

api.add_resource(SomethingAPI, "/Something/API/{}".format(app.config['API_VERSION']))
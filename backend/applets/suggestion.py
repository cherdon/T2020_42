from flask_restful import Resource
from flask import request, jsonify, make_response
from rest_framework import status
from backend.config import db
from backend.helper.recommend import suggestions


class SuggestionAPI(Resource):
    def get(self):
        try:
            name = request.headers.get("API_KEY")
            users = list(filter(lambda person: person['name'] == name, db['customers']))
            if users == []:
                return make_response(jsonify(message="Please provide an API KEY"), status.HTTP_401_UNAUTHORIZED)
            else:
                user = users[0]['name']
                all_suggestions = suggestions[user]['suggested']
                return make_response(jsonify(message=all_suggestions), status.HTTP_200_OK)
        except Exception as e:
            return make_response(jsonify(error=type(e).__name__, message=str(e), args=str(e.args)),
                                 status.HTTP_400_BAD_REQUEST)
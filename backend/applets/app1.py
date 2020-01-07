from flask_restful import Resource
from flask import request, jsonify, make_response
from rest_framework import status
from backend.config import secrets


class SomethingAPI(Resource):
    def get(self):
        keys = request.headers.get("KEY_NAME")
        params = request.args
        try:
            someItem = params.get("someItemKey")
            return make_response(jsonify(response=someItem), status.HTTP_200_OK)
            # return make_response(jsonify(message="No record found"), status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return make_response(jsonify(error=type(e).__name__, message=str(e), args=str(e.args)),
                                 status.HTTP_400_BAD_REQUEST)

    def post(self):
        return None

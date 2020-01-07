from flask_restful import Resource
from flask import request, jsonify, make_response
from rest_framework import status
from backend.config import db
from backend.helper.transactions import breakdown


class TransactionAPI(Resource):
    def get(self):
        try:
            name = request.headers.get("API_KEY")
            params = request.args
            users = list(filter(lambda person: person['name'] == name, db['customers']))
            if users == []:
                return make_response(jsonify(message="Please provide an API KEY"), status.HTTP_401_UNAUTHORIZED)
            else:
                accounts = users[0]['accounts']
                for account in accounts:
                    account_id = account['accountId']
                    if "start" in params:
                        transactions, transaction_breakdown = breakdown(account_id=account_id, start=params['start'], end=params['end'])
                        account['transactions'] = transactions
                        account['breakdown'] = transaction_breakdown
                    else:
                        transactions, transaction_breakdown = breakdown(account_id=account_id)
                        account['transactions'] = transactions
                        account['breakdown'] = transaction_breakdown
                user = users[0]
                user['accounts'] = accounts
                return make_response(jsonify(message=user), status.HTTP_200_OK)
        except Exception as e:
            return make_response(jsonify(error=type(e).__name__, message=str(e), args=str(e.args)),
                                 status.HTTP_400_BAD_REQUEST)
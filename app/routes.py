from app import app
from flask import render_template
import requests


@app.route('/expenditure/<user>')
def expenditure(user):
    headers = {
        "API_KEY": user
    }
    url = app.config['API_URL'] + "/transaction"
    res = requests.get(url, headers=headers).json()
    breakdown = res['message']['accounts'][0]['breakdown']['data']
    transactions = res['message']['accounts'][0]['transactions']
    return render_template('ExpenditurePage.html', user=user, breakdown=breakdown, transactions=transactions)


# params = {
#     "start": "MM-DD-YYYY",
#     "end": "MM-DD-YYYY"
# }
# res = requests.get(url, headers=headers, params=params).json()


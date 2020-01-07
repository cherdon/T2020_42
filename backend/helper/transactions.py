import requests
from backend.config import secrets
import pandas as pd
import json
techtrek = secrets['techtrek']
headers = {
    "identity": techtrek['identity'],
    "token": techtrek['token']
}


def transactions_list(account_id=None, start="01-01-2018", end="01-30-2020"):
    url = techtrek['url'] + "/transactions/" + str(account_id)
    params = {
        "from": start,
        "to": end
    }
    res = requests.get(url, headers=headers, params=params).json()
    return res


def breakdown(account_id=None, start="01-01-2018", end="01-30-2020"):
    all_transactions = transactions_list(account_id=account_id, start=start, end=end)
    df = pd.DataFrame(all_transactions)
    monthly = df
    monthly['amount'] = monthly['amount'].astype(float)
    monthly['date'] = pd.to_datetime(monthly['date'])
    monthly['month'] = monthly['date'].dt.month
    monthly['year'] = monthly['date'].dt.year
    monthly = monthly.groupby(["month", "year", "tag"])['amount'].sum()
    data = json.loads(monthly.to_json(orient="table"))
    return all_transactions, data


if __name__ == "__main__":
    res = transactions_list(account_id=79)
    df = pd.DataFrame(res)
    monthly = df
    monthly['amount'] = monthly['amount'].astype(float)
    monthly['date'] = pd.to_datetime(monthly['date'])
    monthly['month'] = monthly['date'].dt.month
    monthly['year'] = monthly['date'].dt.year
    final = monthly.groupby(["month", "year", "tag"])['amount'].sum()
    print(final)
    data = json.loads(final.to_json(orient="table"))

    print(type(data))
    print(data['data'])

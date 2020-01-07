import requests
from backend.config import secrets
from backend.helper import customer
techtrek = secrets['techtrek']
headers = {
    "identity": techtrek['identity'],
    "token": techtrek['token']
}


def account_list(name=None, id=None):
    if name:
        id = customer.customer_id(name)
    url = techtrek['url'] + "/accounts/deposit/" + str(id)
    res = requests.get(url, headers=headers).json()
    return res


def account_balance(name=None, customer_id=None, account_id=None, month=None, year=None):
    if month:
        params = {
            "month": month-1,
            "year": year
        }
    else:
        params = None
    if name:
        customer_id = customer.customer_id(name)
    if customer_id:
        balances = list()
        accounts = account_list(id=customer_id)
        for account in accounts:
            url = techtrek['url'] + "/accounts/deposit/" + str(account['accountId']) + "/balance"
            if params:
                res = requests.get(url, headers=headers, params=params).json()
            else:
                res = requests.get(url, headers=headers).json()
            balances.append(res)
    if account_id:
        url = techtrek['url'] + "/accounts/deposit/" + account_id + "/balance"
        if params:
            balances = requests.get(url, headers=headers, params=params).json()
        else:
            balances = requests.get(url, headers=headers).json()
    return balances


if __name__ == "__main__":
    # res = account_balance(name="marytan")
    # print(res)
    res = account_balance(customer_id="3")
    print(res)
    # res = account_balance(account_id="10")
    # print(res)



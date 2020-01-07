import requests
from backend.config import secrets
techtrek = secrets['techtrek']
headers = {
    "identity": techtrek['identity'],
    "token": techtrek['token']
}


def customer_id(name):
    url = techtrek['url'] + "/customers/" + name
    res = requests.get(url, headers=headers).json()
    return res


def customer_details(name=None, id=None):
    if name:
        id = customer_id(name)['customerId']
    url = techtrek['url'] + "/customers/" + id + "/details"
    res = requests.get(url, headers=headers).json()
    return res


if __name__ == "__main__":
    res = customer_details(id="2")
    print(res)
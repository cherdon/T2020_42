import requests
from backend.config import secrets
techtrek = secrets['techtrek']
headers = {
    "identity": techtrek['identity'],
    "token": techtrek['token']
}


def marketing_messages():
    url = techtrek['url'] + "/marketing"
    res = requests.get(url, headers=headers).json()
    return res


def marketing_details(id=None):
    url = techtrek['url'] + "/marketing/" + id
    res = requests.get(url, headers=headers).json()
    return res


if __name__ == "__main__":
    res = marketing_messages()
    print(res)
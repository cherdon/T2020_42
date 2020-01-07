import requests
from backend.config import secrets
techtrek = secrets['techtrek']
headers = {
    "identity": techtrek['identity'],
    "token": techtrek['token']
}

def personal_messages(id=None):
    url = techtrek['url'] + "/message/" + id
    res = requests.get(url, headers=headers).json()
    return res

if __name__ == "__main__":
    res = personal_messages('1')
    print(res)
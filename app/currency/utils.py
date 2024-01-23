import json

import requests

from .models import UserRequest


def create_user_request():
    url = "https://economia.awesomeapi.com.br/last/USD-RUB"
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)

    bid = json.loads(response.text)["USDRUB"]["bid"]
    ask = json.loads(response.text)["USDRUB"]["ask"]

    UserRequest.objects.create(bid=bid, ask=ask)

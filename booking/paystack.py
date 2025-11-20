import json
import requests

SECRET_KEY="sk_test_c953a1b007da706c20a189e61547eb97772f1a62"

def paystack(email, amount):
    url = "https://api.paystack.co/transaction/initialize"
    data = {
        "email":email,
        "amount":  int(amount *100),
    }
    header = {
        "Content-Type":"application/json",
        "Authorization": f"Bearer {SECRET_KEY}"
    }
    response=requests.post(url, json=data, headers=header)
    data = response.json()

    auth_url = data["data"]["authorization_url"]
    reference_id = data["data"]["reference"]

    return{"authorization_url":auth_url, "reference_id":reference_id}
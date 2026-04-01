import requests

FLASK_URL = "http://mock-server:5000/api/customers"

def fetch_all_customers():
    page = 1
    limit = 10
    all_data = []

    while True:
        res = requests.get(FLASK_URL, params={"page": page, "limit": limit}).json()
        data = res["data"]

        if not data:
            break

        all_data.extend(data)
        page += 1

    return all_data
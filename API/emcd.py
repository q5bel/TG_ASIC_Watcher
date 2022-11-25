import requests

from data import EMCD_TOKEN

url = 'https://api.emcd.io/v1/btc/workers/' + EMCD_TOKEN


def emcd_request():
    response = requests.get(url)
    data = response.json()
    total_count = data["total_count"]
    active = total_count["active"]
    inactive = total_count["inactive"]
    print('Making request to EMCDpool')
    return f'EMCD pool \n\nНеактивные воркеры: {inactive} \nРабота в нормальном режиме: {active}'


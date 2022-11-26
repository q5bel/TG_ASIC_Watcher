import requests
from datetime import datetime

from data import EMCD_TOKEN

url = 'https://api.emcd.io/v1/btc/workers/' + EMCD_TOKEN


def emcd_request():
    response = requests.get(url)
    data = response.json()
    total_count = data["total_count"]
    active = total_count["active"]
    inactive = total_count["inactive"]
    print(f'Making request to EMCDpool. {datetime.now()}')
    return f'🏧 EMCD pool \n\n❌ Неактивные воркеры: {inactive} \n✅ Работа в нормальном режиме: {active} из 4'


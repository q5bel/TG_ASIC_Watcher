import hashlib
import hmac
import time

import requests
import json

from data import ANTPOOL_TOKEN, ANTPOOL_SECRET, SIGN_ID


def get_signature():
    nonce = int(time.time() * 1000)
    msgs = SIGN_ID + ANTPOOL_TOKEN + str(nonce)
    ret = []
    ret.append(hmac.new(ANTPOOL_SECRET.encode(encoding="utf-8"), msg=msgs.encode(encoding="utf-8"),
                        digestmod=hashlib.sha256).hexdigest().upper())
    ret.append(nonce)
    return ret


def get_overview():
    api_sign = get_signature()
    post_data = {'key': ANTPOOL_TOKEN, 'nonce': api_sign[1], 'signature': api_sign[0],
                 'coin': 'BTC', 'userId': SIGN_ID}
    request = requests.post('https://antpool.com/api/accountOverview.htm', data=post_data)
    return request.text


def ant_request():
    data = json.loads(get_overview())
    data_in_data = data["data"]
    inactiveWorkerNum = data_in_data['inactiveWorkerNum']
    activeWorkerNum = data_in_data['activeWorkerNum']
    print('Making request to antpool')
    return f'ANTPOOL {SIGN_ID} \n\nНеактивные воркеры: {inactiveWorkerNum} \nРабота в нормальном режиме: {activeWorkerNum}'

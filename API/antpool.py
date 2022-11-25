import hashlib
import hmac
import time

import requests

from data import *

html_overview = 'https://antpool.com/api/accountOverview.htm'


def get_signature():
    nonce = int(time.time() * 1000)
    msgs = SIGN_ID + ANTPOOL_TOKEN + str(nonce)
    ret = []
    ret.append(hmac.new(ANTPOOL_SECRET.encode(encoding="utf-8"), msg=msgs.encode(encoding="utf-8"),
                        digestmod=hashlib.sha256).hexdigest().upper())
    ret.append(nonce)
    return ret


def get_overview(url):
    api_sign = get_signature()
    post_data = {'key': ANTPOOL_TOKEN, 'nonce': api_sign[1], 'signature': api_sign[0],
                 'coin': 'BTC', 'userId': SIGN_ID}
    request = requests.post(url, data=post_data)
    return request.text


def main():
    print(get_overview(html_overview))


main()

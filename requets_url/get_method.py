import requests
import json
from requets_url import logutil2
def get_method(url,data):
    res = requests.get(url=url,data=data)
    loger = logutil2.logs()
    if res.status_code == 200:

        loger.info("返回成功")
    else:
        loger.error("返回失败！")

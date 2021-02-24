import requests
import json
from config import readConfig
def get_token():
    base_url = readConfig.getConfig("URL","base_url")
    print("base_url:%s"%base_url)
    api_url = "/blade-auth/token"
    url =base_url+api_url
    #url = "http://192.168.2.73:999/blade-auth/token"
    header = {"Accept": "application/json",
              "Authorization": "Basic YW5jaG9yOmFuY2hvcl9zZWNyZXQ=",
              "User-Type": "ORGAN"}
    data = {
        "account": "linsn",
        "password": "123456",
        "grantType": "password"
    }  # 多行文本, 字符串格式，也可以单行（注意外层有引号，为字符串） data = '{"name": "hanzhichao", "age": 18}'
    res = requests.post(url=url, headers=header, data=data)  # data支持字典或字符串
    #print(res.text)
    resonse = json.loads(res.text)
    print(resonse)
    token = resonse["data"]["accessToken"]
    print(token)

    return token

if __name__=="__main__":

    # header = {"Accept": "application/json",
    #           "Authorization": "Basic YW5jaG9yOmFuY2hvcl9zZWNyZXQ=",
    #           "User-Type": "KH"}
    # data = {
    #     "account": "admin",
    #     "password": "123456",
    #     "grantType": "password"
    # }
    token = get_token()
    print("token:%s"%token)
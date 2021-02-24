import requests
import json
from requets_url import logutil2
class HandleRequests:
    def __init__(self):
        self.loger = logutil2.Logs()
    def get(self, url, **kwargs):
        """封装get方法"""
        # 获取请求参数
        params = kwargs.get("params")
        headers = kwargs.get("headers")
        try:
            result = requests.get(url, params=params, headers=headers)
            return result
        except Exception as e:
            print("get请求错误: %s" % e)
    def post(self, url, **kwargs):
        """封装post方法"""
        # 获取请求参数
        params = kwargs.get("params")
        data = kwargs.get("data")
        json = kwargs.get("json")
        try:
            result = requests.post(url, params=params, data=data, json=json)
            return result
        except Exception as e:
            print("post请求错误: %s" % e)
            self.loger.error(e)

    def post_res(self,res):
        print("status_code:%s"%type(res))

        if res.status_code == 200:
            self.loger.info("返回成功")
        else:
            self.loger.error("返回失败！"+res.url+res.text)

    def get_res(self,res):
        print("status_code:%s"%type(res))

        if res.status_code == 200:
            self.loger.info("get请求返回成功")
        else:
            self.loger.error("get返回失败！"+res.url+res.text)


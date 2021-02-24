import xlrd
import requests
import json
from requets_url import get_token
from requets_url import handlerequests
class ReadExcel:
    def __init__(self):
        print("hello")
    def excel_to_list(self,data_file,sheet):
        data_list = []
        wb = xlrd.open_workbook(data_file)
        sh = wb.sheet_by_name(sheet)
        header = sh.row_values(0)
        for i in range(1,sh.nrows):
            d = dict(zip(header,sh.row_values(i)))
            data_list.append(d)
        return data_list

    def get_test_data(self,data_list,case_name):
        for case_data in data_list:
            if case_name == case_data['case_name']:
                return case_data
            else:
                None


#
# if __name__ == '__main__':
#     re = ReadExcel()
#     mt = method.Method()
#     data_list = re.excel_to_list("D://python//api_test//data//url.xlsx","Sheet1")
#     print(data_list)
#     case_data = re.get_test_data(data_list,"test_login")
#     print(case_data)
#     for case in data_list:
#
#         headers = case['headers']
#         print(type(headers))
#         method = case['method']
#         url = case['url']
#         data = case['data']
#         print(method)
#         if method == "POST":
#             print("method is post")
#             if headers == '':
#                 res = mt.post_method(url=url, data=data)
#                 #res = requests.post(url=case['url'], data=case['data'])
#             else:
#
#                 if "blade-auth" in json.loads(headers).keys():
#                     print("token is ")
#                     headers = json.loads(headers)
#                     token = get_token.get_token()
#                     print("token:%s" % token)
#                     print(type(token))
#
#                     headers["blade-auth"] = "bearer " + get_token.get_token()
#                     print(headers["blade-auth"])
#                     res = requests.post(url=url, headers=headers, data=data)
#                 else:
#                     res = requests.post(url=url, headers=json.loads(headers), data=data)
#                     print(res.text)

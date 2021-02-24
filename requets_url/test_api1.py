import unittest
from requets_url import get_token
from requets_url import handlerequests
from requets_url import logutil2
from requets_url import read_excel
import json
from HTMLTestRunner import HTMLTestRunner
from requets_url import send_mail
import time
import os


class MyTestCase(unittest.TestCase):

    def setUp(self):
        print('...setup...')
        # 用例路径
        self.case_path = "D:\\python\\interface_test"
        print(self.case_path)

    def test_api(self):
        re = read_excel.ReadExcel()
        mt = handlerequests.HandleRequests()
        data_list = re.excel_to_list("D://python//api_test//data//url.xlsx", "Sheet1")
        print(data_list)
        # case_data = re.get_test_data(data_list,"test_login")
        # print(case_data)

        for case_data in data_list:

            headers = case_data['headers']
            print(type(headers))
            method = case_data['method']
            url = case_data['url']
            data = case_data['data']
            print(method)
            if method == "POST":
                print("method is post")
                if headers == '':
                    res = mt.post(url=url, data=data)
                    mt.post_res(res)
                    # res = requests.post(url=case['url'], data=case['data'])
                else:
                    if "blade-auth" in json.loads(headers).keys():
                        print("token is ")
                        headers = json.loads(headers)
                        token = get_token.get_token()
                        print("token:%s" % token)
                        print(type(token))

                        headers["blade-auth"] = "bearer " + get_token.get_token()
                        print(headers["blade-auth"])
                        res = mt.post(url=url, headers=headers, json=data)
                        mt.post_res(res)
                    else:
                        res = mt.post(url=url, json=data, headers=json.loads(headers))
                        mt.post_res(res)
                        staus_code = res.status_code
                        print("status_code:%s" % staus_code)
                        print("res.text:%s" % res.text)
            else:
                res = mt.get(url=url, params=data)
                mt.get_res(res)

    def tearDown(self):
        pass

    def creatsuite(self):  # 创建测试用例集
        # testSuite = unittest.TestSuite()
        # testSuite.addTest(test_baidu.MyTest("test_baidu"))
        testsuite = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(
            start_dir=self.case_path,
            pattern="test*.py",
            top_level_dir=None,
        )
        for allcase in discover:
            for case in allcase:
                print(case)
                testsuite.addTests(case)
        return testsuite


# if __name__ == '__main__':
#     print("hello")
#     now = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
#     report_path = os.getcwd()
#     # 2、html报告文件路径
#     filename = os.path.join(report_path, now + "result.html")
#     print("测试报告路径==========================>", filename)
#
#     # 3、打开一个文件，将result写入此file中
#     fp = open(filename, 'wb')
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
#                                            title="chen测试用例",
#                                            description="测试情况，如下：",
#                                            verbosity=2)
#     # 4、调用add_case函数返回值
#     runner.run(MyTestCase.creatsuite())
#     fp.close()
#     # send_email('report.html')
#     send_mail.SendMail().send_email(filename)

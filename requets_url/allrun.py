import sys

from requets_url import get_token
from requets_url import handlerequests
from requets_url import logutil2
from requets_url import read_excel
import json
import unittest
import os,time
from HTMLTestRunner import HTMLTestRunner
from requets_url import send_mail

#获取当前文件allrun_case.py的绝对路径
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

print(root_path)

now = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
report_path = ("..\\report")
# 2、html报告文件路径
filename = os.path.join(report_path, now + "result.html")
suite = unittest.defaultTestLoader.discover("./")
with open(filename, 'wb') as f:  # 改为with open 格式
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述").run(suite)

# send_email('report.html')
sm = send_mail.SendMail()
report_file=sm.new_report("..\\report")
sm.send_email(filename)

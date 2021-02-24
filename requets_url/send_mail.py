import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from config import readConfig
from requets_url import logutil2
import os
from pathlib import Path

class SendMail():

    def __init__(self):
        self.sender = readConfig.getConfig("EMAIL", "sender")
        self.mail_pass = readConfig.getConfig("EMAIL", "mail_pass")
        self.receiver = readConfig.getConfig("EMAIL", "receiver")
        self.mail_host = readConfig.getConfig("EMAIL", "mail_host")
        self.logger = logutil2.Logs()

    # 定义发送邮件
    def new_report(self, testreport):
        lists = os.listdir(testreport)
        lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))  # 获取一个文件中的最近访问时间的文件
        file_new = os.path.join(testreport, lists[0])
        print("==========获取最近时间生成的报告文件路径===========>" + file_new)
        return file_new

    def send_email(self, reprot_file):
        msg = MIMEMultipart()  # 混合MIME格式
        msg.attach(MIMEText(open(reprot_file, encoding='utf-8').read(), 'html', 'utf-8'))  # 添加HTML格式邮件正文

        msg['From'] = self.sender
        msg['To'] = self.receiver
        msg['Subject'] = Header("自动化测试报告", 'utf-8')  #设置邮件标题
        att1 = MIMEText(open(reprot_file, 'rb').read(), 'html', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["content-Disposition"] = 'attachment;filename="report.html"'  # filename为邮件中附件显示的名字
        msg.attach(att1)

        try:
            smtp = smtplib.SMTP_SSL(self.mail_host)
            smtp.login(self.sender, self.mail_pass)
            smtp.sendmail(self.sender, self.receiver, msg.as_string())
            self.logger.info("邮件发送完成")
        except Exception as e:
            self.logger.error(str(e))
        finally:
            smtp.quit()

# if __name__ == '__main__':
#     sm = SendMail()
#     report_file=sm.new_report("..\\report")
#     path = Path(report_file)
#     print("path%s"%path)
#
#     f = open(report_file, 'rb').read()
#     print(f)
#     sm.send_email(report_file)

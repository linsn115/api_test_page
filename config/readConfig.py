import os
import configparser

def getConfig(section,key):
    config = configparser.ConfigParser()
    #获取配置文件的真实路径
    path = os.path.split(os.path.realpath(__file__))[0] + '\config.ini'
    print(path)
    #print("获取配置文件的真实路径为："+path)
    config.read(path,encoding="utf-8")
    return config.get(section,key)

if __name__ == "__main__":
    sender = getConfig("EMAIL", "sender")
    print(sender)

# -*- coding:utf-8 -*-
import requests
import time
import getbasedata
import pretreat
import json

"""
这个模块用来向服务器发送监控数据
"""

#服务器ip
SERVICE_ADDR = "10.10.10.14:8000"
#webAPI
PUSH_API = "/factory/pushdata/"

def push_host_data():
    #获取系统信息
    thehost = getbasedata.GetBaseinfo()
    general_info = pretreat.Pretreat.get_general_info()
    cpu_info = thehost.get_cpu()
    mem_info = thehost.get_memory()
    disk_info = thehost.get_disk()
    #预处理系统信息
    host_info = pretreat.Pretreat.host_info_pre(
        general_info,cpu_info,mem_info,disk_info)
    #向服务器推送系统信息
    urltmp = ["http://",SERVICE_ADDR,PUSH_API]
    url = ''.join(urltmp)
    response = requests.post(url,data=host_info)
    return response


if __name__  == "__main__":
#   while True:
        d = push_host_data()
        f = open("/opt/mysite/factory/templates/factory/text.html","w")
        f.write(d.text)
        time.sleep(1)
#       print(d.text)
#   a = response.status_code
#   b = response.content
#   c = response.headers
#   d = response.text

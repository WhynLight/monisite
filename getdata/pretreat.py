# -*- coding:utf-8 -*-
import json
import time
import getbasedata

SERVICE_ADD = "10.10.10.14"
PUSH_API = "/factory/pushdata"

class Pretreat(object):
    """
    这个类用作发送请求前数据的预处理
    """

    @staticmethod
    def get_general_info():
        """
        获取系统当前的时间戳
        参数：无
        返回值：字典类型
        字典键值:
            "timestame":str类型十位时间戳
        """
        timestame = int(time.time())
        general_info = {"timestame":timestame}
        return general_info

    @staticmethod
    def host_info_pre(general_info,cpu_info,mem_info,disk_info):
        """
        系统基础信息如系统时间，cpu等信息的预处理
        参数：
            general_info:系统当前时间戳
            cpu_info:cpu信息
            mem_info:内存信息
            disk_info:磁盘信息
            host_name:主机名
        返回值：
            host_info:json对象，包含系统基础信息
        """
        #主机名修改host_name实现
        host_info = {
            "general_info":general_info,
            "cpu_info":cpu_info,
            "mem_info":mem_info,
            "disk_info":disk_info,
            "host_name":"myserver"
            }
        host_info = json.dumps(host_info)
        return host_info

if __name__ == "__main__":
    a = Pretreat.get_general_info()
    b = Pretreat.host_info_pre(1,2,3,4)
    print(a,type(a))
    print(b,type(b))

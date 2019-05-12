# -*- coding:utf-8 -*-
import json
from factory.models import Cpudata,Memorydata,Diskdata,Lastcomm


class Operfact(object):
    """
    这个类用于将监控数据插入数据库
    """
    
    @staticmethod
    def save_hostinfo(host_info):
        """   
        这个方法用来将系统信息插入数据库
        参数：
            host_info:字典类型，格式如下：
            {
                "general_info":{
                    "host_ip":"xxx.xxx.xxx.xxx",    #str类型
                    "timestame":"xxxxxxxxxx"    #十位时间戳,str类型
                },
            
                "cpu_info":{
                    "cpu_percent":"xxxxx"   #str类型
                },
            
                "mem_info":{
                    "mem_percent":"xx.x",   #str类型
                    "mem_free":"xxxx"   #str类型
                },
            
                "disk_info"{
                    "disk_percent":"xx.x", #str类型
                    "disk_free":"xxxx"  #str类型
                },
                "host_name":"hostname"
            
            }
        """
        #存入cpu信息
        Cpudata.objects.create(timestame=host_info["general_info"]["timestame"],
            host_ip=host_info["general_info"]["host_ip"],
            cpu_percent=host_info["cpu_info"]["cpu_percent"])
        #存入内存信息
        Memorydata.objects.create(timestame=host_info["general_info"]["timestame"],
            host_ip=host_info["general_info"]["host_ip"],
            mem_percent=host_info["mem_info"]["mem_percent"],
            mem_free=host_info["mem_info"]["mem_free"])
        #存入磁盘信息
        Diskdata.objects.create(timestame=host_info["general_info"]["timestame"],
            host_ip=host_info["general_info"]["host_ip"],
            disk_percent=host_info["disk_info"]["disk_percent"],
            disk_free=host_info["disk_info"]["disk_free"])

        #此主机信息如果已存在于Lastcomm表，则更新timestame列
        #否则创建一条新记录
        if len(Lastcomm.objects.filter(host_ip=host_info["general_info"]["host_ip"])) == 1:
            Lastcomm.objects.filter(host_ip=host_info["general_info"]["host_ip"]).update(timestame=host_info["general_info"]["timestame"])
        else:
            Lastcomm.objects.create(timestame=host_info["general_info"]["timestame"],
                host_name=host_info["host_name"],
                host_ip=host_info["general_info"]["host_ip"])

    def take_lastcomm():
        """
        这个函数用来获取Lastcomm表中所有主机ip
        """
        host_data = dict()
        hosts = list(Lastcomm.objects.all().values("host_ip"))
        #for i in hosts:
        #    del i["id"]
        #    i["cpu_percent"] = Cpudata.objects.get(host_ip=i["host_ip"],timestame=i["timestame"]).cpu_percent
        #    i["mem_percent"] = Memorydata.objects.get(host_ip=i["host_ip"],timestame=i["timestame"]).mem_percent
        #    i["disk_percent"] = Diskdata.objects.get(host_ip=i["host_ip"],timestame=i["timestame"]).disk_percent
        #    host_data[i["host_ip"]] = i
        return json.dumps(hosts)

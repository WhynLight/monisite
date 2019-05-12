# -*- coding:utf-8 -*-
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import time
import json
import os,sys
from factory.models import Cpudata,Memorydata,Diskdata,Lastcomm
from alarms.models import Threvalue


class Opersite(object):

    @staticmethod
    def single_column(name):
        """
        这个函数用来获取Lastcomm表中所有主机ip
        返回值: list类型，所有ip的列表
        """
        data = list(Lastcomm.objects.all().values("host_ip"))
        return json.dumps(hosts)

    @staticmethod
    def take_img(ip,valname,imgpath):
        """
        参数:ip:str类型，生成折线图的主机ip
            valname:str类型，生成折线图对应的主机性能指标
            imgpath:str类型，折线图存储目录的绝对路径
        这个函数用来生成对应ip和性能数据的折线图
        返回值:str类型的图片路径
        """
        #删除可能已经存在的图片
        if os.path.exists(imgpath):
            filelist = os.listdir(imgpath)
            for f in filelist:
                timediff = int(time.time())-int(f[:-4])
                if timediff>6:
                    f = os.path.join(imgpath,f)
                    os.remove(f)
        else:
            os.makedirs(imgpath)

        imgpath = imgpath + str(int(time.time())) + ".png"

        #定义x轴和y轴
        x = list()
        y = list()
        #从数据库中取出监控数据
        if valname == "cpu_percent":
            host_data = Cpudata.objects.filter(host_ip=ip).order_by("-timestame")[:60].values("cpu_percent","timestame")
        elif valname == "mem_percent":
            host_data = Memorydata.objects.filter(host_ip=ip).order_by("-timestame")[:60].values("mem_percent","timestame")
        elif valname == "disk_percent":
            host_data = Diskdata.objects.filter(host_ip=ip).order_by("-timestame")[:60].values("disk_percent","timestame")
        #将数据取出到xy轴
        for i in host_data:
            y.append(i[valname])
            time_array = time.localtime(i["timestame"])
            x.append(time.strftime("%H:%M:%S",time_array))
        x = x[::-1]
        y = y[::-1]
        #设置x轴间隔
        tick_spacing = 10
        #创建图表
        fig,ax = plt.subplots(1,1)
        ax.plot(x,y)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        plt.savefig(imgpath,format="png")
        plt.close()
        imgpath = imgpath.strip(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        imgpath = "/"+imgpath

        print("++++++++++++++++++++++++++++++")
        print(imgpath)
        return imgpath

        
    @staticmethod
    def take_hostdata(ip):
        """
        这个函数查询某个主机最新的性能数据
        参数:ip:str类型，需要查询主机的ip
        返回值：dict类型,键-值为 性能数据类型-对应的性能数据的值
        """
        #获取最近一次主机提交的数据
        host_data = dict()
        host_time = Lastcomm.objects.get(host_ip=ip).timestame
        host_data["cpu"] =  Cpudata.objects.get(host_ip=ip,timestame=host_time).cpu_percent
        host_data["mem"] = Memorydata.objects.get(host_ip=ip,timestame=host_time).mem_percent
        host_data["disk"] = Diskdata.objects.get(host_ip=ip,timestame=host_time).disk_percent

        return host_data




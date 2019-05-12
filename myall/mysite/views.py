from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from factory.models import Cpudata,Memorydata,Diskdata,Lastcomm
from alarms.models import Threvalue
from mysite.opersite import Opersite
import json
import os,sys

def hoststatus(request):
    """
    根据请求传值判断执行动作
    """
    content = dict()
    content["hostip"] = json.dumps(list(Lastcomm.objects.all().values("host_ip","host_name","alarm_rule")))
    content["ala_name"] = json.dumps(list(Threvalue.objects.all().values()))
    #content["ala_name"] = json.dumps(list(Threvalue.objects.all().values("thre_name")))

    if request.GET.keys():
        """
        GET请求数据为dict类型，格式为:
        {"refre":"xxx",
        "alarm_opt":"xxx",
        "alarm_host":"xxx",
        "last_data":"xxx",
        "take_img":"xxx"}
        """
        #取出GET数据的键，解码后为dict类型
        host_ip = next(iter(request.GET.keys()))
        host_ip = json.loads(host_ip)

        #GET传refre键的值则生成对应主机性能图片并发送最新监控数据
        if host_ip["refre"]:
            host_ip = host_ip["refre"]
            detail = Opersite.take_hostdata(host_ip)
            cpu_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/static/myall/images/cpu/'
            mem_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/static/myall/images/mem/'
            disk_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/static/myall/images/disk/'
            detail["cpuimg"] = Opersite.take_img(host_ip,"cpu_percent",cpu_path)
            detail["memimg"] = Opersite.take_img(host_ip,"mem_percent",mem_path)
            detail["diskimg"] = Opersite.take_img(host_ip,"disk_percent",disk_path)
            return HttpResponse(json.dumps(detail))

        #存放下拉菜单传递的主机对应阀值配置
        if host_ip["alarm_opt"]:
            Lastcomm.objects.filter(host_name=host_ip["alarm_host"]).update(alarm_rule=host_ip["alarm_opt"])

        #取出对应主机最新的监控数据
        if host_ip["last_data"]:
            resdata = Opersite.take_hostdata(host_ip["last_data"])
            return HttpResponse(json.dumps(resdata))

    return render(request,'mysite/hoststatus.html',content)

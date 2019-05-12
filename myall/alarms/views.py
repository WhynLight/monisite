# -*- coding:utf-8 -*-
from django.shortcuts import render
from alarms.models import Threvalue
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from alarms.operalarm import Operthre
import ast
import json
# Create your views here.

def alarms(request):
    """
    这个函数用于访问告警子页面
    """
    content = dict()
    content["thre_val"] = json.dumps(Operthre.take_thre())
    return render(request,'alarms/alarms.html',content)

@csrf_exempt
def savethre(request):
    """
    这个方法用于将表单post的阀值配置数据写入数据库
    """
    #提取数据
    thre_val = {}
    if request.POST:
        post_val = dict()
        for key in request.POST:
            post_val = ast.literal_eval(key)
        thre_val["thre_name"] = post_val["threname"]
        thre_val["cpu_thre"] = post_val["cputhre"]
        thre_val["mem_thre"] = post_val["memthre"]
        thre_val["disk_thre"] = post_val["diskthre"]
    #写入数据库
    Threvalue.objects.create(thre_name=str(thre_val["thre_name"]),
        cpu_thre=int(thre_val["cpu_thre"]),
        memory_thre=int(thre_val["mem_thre"]),
        disk_thre=int(thre_val["disk_thre"])
        )

    #return render(request,"alarms/test.html",content)
    return render(request,"alarms/alarms.html")

def delthre(request):
    """
    这个方法用来删除某一条阀值配置数据
    返回值：hand_result:str类型，成功为success,失败为failed
    """
    if request.POST:
        post_val = list(request.POST.keys())[0]
        hand_result = Operthre.del_thre(post_val)
    return HttpResponse(hand_result)

# -*- coding:utf-8 -*-
import json
from django.shortcuts import render
from django.http import HttpResponse
from factory.models import Cpudata,Memorydata,Diskdata,Lastcomm
from factory.operfact import Operfact
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):

    return HttpResponse("aaaaaaaaaaaaaaaa")

@csrf_exempt
def pushdata(request):
    """
    这个函数获取agent推送的数据并存入数据库
    """
    host_info = json.loads(request.body)
    host_info["general_info"]["host_ip"] = request.META["REMOTE_ADDR"]
    save_result = ""
    try:
        a = Operfact.save_hostinfo(host_info)
    except:
        save_result = "failed"
    else:
        save_result = "success"
    return HttpResponse(save_result)

@csrf_exempt
def test(request):
#   a = json.loads(request.body)
    return render(request,'factory/text.html')
#   return HttpResponse("dddddddddddddddddddddd")


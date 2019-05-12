# -*- coding:utf-8 -*-
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import os
import time
from factory.models import Cpudata,Memorydata,Diskdata,Lastcomm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from io import BytesIO
import base64
#a = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def quer(request):
    
    ip = "10.10.10.13"
    x = list()
    y = list()
    imgpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/static/myall/images/1.png'
    host_data = Cpudata.objects.filter(host_ip=ip).order_by("-timestame")[:60].values("cpu_percent","timestame")
    for i in host_data:
        y.append(i["cpu_percent"])
        time_array = time.localtime(i["timestame"])
        x.append(time.strftime("%H:%M:%S",time_array))
    x = x[::-1]
    y = y[::-1]

    tick_spacing = 10
    fig, ax = plt.subplots(1,1)
    ax.plot(x,y)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.savefig(imgpath,format="png")
    plt.close()

#   plt.plot(x,y,linewidth=5)
#   plt.title("Cpu data",fontsize=20)
#   plt.xlabel("time",fontsize=5)
#   plt.ylabel("cpu percent",fontsize=5)
#   plt.tick_params(axis="both",labelsize=10)
#   plt.savefig(imgpath,format="png")
#   plt.close()
    return HttpResponse(host_data)

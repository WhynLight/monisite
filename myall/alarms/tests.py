# -*- coding:utf-8 -*-
from django.test import TestCase
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from alarms.operalarm import Operthre
import json

#@csrf_exempt
def testdemo(request):
    content = dict()
    content["threval"] = json.dumps(Operthre.take_thre())
    #content = json.dumps(content)
    return render(request,"alarms/test.html",content)

# Create your tests here.

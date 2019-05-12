# -*- coding:utf-8 -*-
from django.db import models

class Threvalue(models.Model):
    """
    Threvalue表存放各个性能指标的报警阀值
    """
    thre_name = models.CharField(max_length=20)
    cpu_thre = models.FloatField(default=False)
    memory_thre = models.IntegerField(default=False)
    disk_thre = models.BigIntegerField(default=False)



# Create your models here.

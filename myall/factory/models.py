# -*- coding:utf-8 -*-
from django.db import models

class Cpudata(models.Model):
    """
    CpuData表存放cpu性能信息
    """
    timestame = models.IntegerField()
    host_ip = models.CharField(max_length=20)
    cpu_percent = models.FloatField()

class Memorydata(models.Model):
    """
    MemoryData表存放系统内存信息
    """
    timestame = models.IntegerField()
    host_ip = models.CharField(max_length=20)
    mem_percent = models.FloatField()
    mem_free = models.IntegerField()

class Diskdata(models.Model):
    """
    DiskData表存放系统磁盘信息
    """
    timestame = models.IntegerField()
    host_ip = models.CharField(max_length=20)
    disk_percent = models.FloatField()
    disk_free = models.BigIntegerField()

class Lastcomm(models.Model):
    """
    Lastcomm表存放客户端最后一次向服务器发送数据的时间戳
    """
    host_name = models.CharField(max_length=20,default=False)
    alarm_rule= models.CharField(max_length=20,default=False)
    host_ip = models.CharField(max_length=20)
    timestame = models.IntegerField()



# Create your models here.

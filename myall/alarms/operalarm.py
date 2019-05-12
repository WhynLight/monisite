# -*- coding:utf-8 -*-
from alarms.models import Threvalue
import json

class Operthre(object):
    """
    这个类用于对阀值数据的操作
    """

    @staticmethod
    def take_thre():
        """
        这个方法用于从Threvalue表中取出阀值配置数据
        返回值类型:字典类型的列表
        返回值格式:e.g.:[{"nid": 2, "course": "python"}, {"nid": 24, "course": "python"}]

        """
        query_val = Threvalue.objects.all().values()
        threval = []
        for i in query_val:
            threval.append(i)
        return threval
        
    @staticmethod
    def del_thre(del_name):
        """
        从数据库删除某一条阀值配置数据
        参数:del_name:str类型，数据的名称，对应数据库的thre_name列
        返回值:del_result:str类型，成功为success，否则为failed
        """
        del_result = str()
        try:
            data = Threvalue.objects.get(thre_name=del_name)
        except:
            del_result = "failed"
        else:
            data.delete()
            del_result = "success"
        return del_result
            

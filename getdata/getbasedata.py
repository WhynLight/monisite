# -*- coding:utf-8 -*-
import psutil

class GetBaseinfo(object):
    """
    这个类用来收集操作系统基础信息，例如：
    cpu信息
    内存信息
    磁盘信息
    """

    def get_cpu(self):
        """
        这个方法用来收集cpu相关信息
        参数：无
        返回值：cpu_info（字典类型,键-值 分别为 cpu使用情况指标-指标数值）
        指标说明:
            cpu_percnet:cpu使用率
        """
        cpu_percent =  psutil.cpu_percent()

        cpu_info = {"cpu_percent":cpu_percent}
        return cpu_info

    def get_memory(self):
        """
        这个方法用来收集系统内存信息
        参数：无
        返回值：mem_info(字典类型，键-值 分别为 内存使用情况指标-指标数值)
        指标说明：
                mem_percent:内存使用率
                mem_free:空闲内存
        """
        mem = psutil.virtual_memory() 
        mem_percent = mem.percent
        mem_free = mem.free

        mem_info = {"mem_percent":mem_percent,
                    "mem_free":mem_free}
        return mem_info 

    def get_disk(self):
        """
        这个方法用来收集系统磁盘信息
        参数：无
        返回值：disk_info(字典类型，键-值 分别为 磁盘使用情况指标-指标数值)
        指标说明：
                disk_percnet:磁盘使用率
                disk_free:磁盘剩余空间，单位为kb
        """
        disk = psutil.disk_partitions()

        mount_point = disk[0].mountpoint
        disk_usage = psutil.disk_usage(mount_point)
        disk_percent = disk_usage.percent
        disk_free = disk_usage.free

        disk_info = {"disk_percent":disk_percent,
                     "disk_free":disk_free}
        return disk_info





if __name__ == "__main__":
    myhost = GetBaseinfo()
    cpu_info = myhost.get_cpu()
    mem_info = myhost.get_memory()
    disk_info = myhost.get_disk()
    print("cpu信息: ",cpu_info)
    print("mem信息: ",mem_info)
    print("disk信息 ",disk_info)

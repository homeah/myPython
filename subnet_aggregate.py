#!/usr/bin/python 
from netaddr import IPAddress,IPNetwork,cidr_merge
import os.path
def subnet_aggregate(ip_file):
    listIP = []
    f = open(ip_file)
    for each in f:
        if each.isspace():
            continue
        listIP.append(IPNetwork(each))
    temp_list = cidr_merge(listIP)
    for each in temp_list:
        print(each)

ip_file = input('请输入的IP子网的文件名：')
while(not os.path.exists(ip_file)):
    print("文件名不存在，请重新输入!")
    ip_file = input('请输入的IP子网的文件名：')
try:
    subnet_aggregate(ip_file)
except:
    print('IP内文件格式不对！')




    

#! /etc/bin/env python
#coding:utf-8
import pexpect
import sys
import time
import getpass
ip = input('请输入设备IP：')
user = input('请输入你的用户名：')
passwd = getpass.getpass()
time1 = time.strftime('%Y-%m-%d-%H:%M',time.localtime(time.time()))
child = pexpect.spawn('/usr/bin/ssh',[user+'@'+ip],timeout=20,maxread = 200000,searchwindowsize = 200)
f = open(ip+'-'+time1,'wb')
child.logfile = f
child.expect('password: ')
child.sendline(passwd)
print('请等候....')
child.expect('.*#')
child.sendline('terminal length 0')
child.expect('.*#')
child.sendline('sh int | i pro|Des|rate')
child.expect('.*#',timeout = 30)
child.sendline('exit')
f.close() 
def sortpacket(file):
    dict1 ={}
    des = 'None'
    with open(file,'r') as f:
        lines = f.readlines()
        for line in lines:
            if 'Gig' in line and 'Description' not in line: #逐行读取，发现Gig字符，存储接口
               interface = line.partition(' ')[0]
            if 'Description' in line:
                des = line.split(':')[1].strip()
            if 'input rate' in line:
                #逐行读取，发现input后，以空格切片，第4个字符是速率，第6个是包量
                inbps,inpps = int(line.split()[4]),int(line.split()[6])    
            if 'output rate' in line:
                outbps,outpps = int(line.split()[4]),int(line.split()[6])
                dict1[interface] = (des,inbps,inpps,outbps,outpps)
        #以包量排序
        a = int(input('1.入向流量排序 2.入向包量排序 3.出向流量排序 4.出向包量排序 请选择1、2、3、4：'))
        while True:
            if a == 1:
                temp = sorted(dict1.items(),key = lambda x:x[1][1],reverse = True)
                print('TOP50接口入向流量排名：')
                i = 0
                for each in temp:
                    if i < 50:
                        print('%-30s%-40s%dbps' %(each[0],each[1][0],each[1][1]))
                        i += 1
                    else:
                        break
            elif a == 2:
                temp = sorted(dict1.items(),key = lambda x:x[1][2],reverse = True)
                print('TOP50接口入向包量排名')
                i = 0
                for each in temp:
                    if i < 50:
                        print('%-30s%-40s%dpps' %(each[0],each[1][0],each[1][2]))
                        i += 1
                    else:
                        break
            elif a ==3:
                temp = sorted(dict1.items(),key = lambda x:x[1][3],reverse = True)
                print('TOP50接口出向流量排名')
                i = 0
                for each in temp:
                    if i <50:
                        print('%-30s%-40s%dbps' %(each[0],each[1][0],each[1][3]))
                        i += 1
                    else:
                        break
            elif a == 4:
                temp = sorted(dict1.items(),key = lambda x:x[1][4],reverse = True)
                print('TOP50接口出向包量排名')
                i = 0
                for each in temp:
                    if i < 50:
                        print('%-30s%-40s%dpps' %(each[0],each[1][0],each[1][4]))
                        i+= 1
                    else:
                        break
            else:
                print('输入有误！')
            yes_no = input('是否继续查看? Y/y or N/n：')
            if yes_no == ('y' or 'Y'):
                a = int(input('1.入向流量排序 2.入向包量排序 3.出向流量排序 4.出向包量排序 请选择1、2、3、4：'))
            else:
                break
sortpacket(ip+'-'+time1)

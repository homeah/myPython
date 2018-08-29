#!/bin/python
def sortpacket(file):
    dict1 ={}
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
        a = int(input('1.入向流量排序 2.入向包量排序 3.出向流量排序 4 出向包量排序，请选择1、2、3、4：'))
        if a == 1:
            temp = sorted(dict1.items(),key = lambda x:x[1][1],reverse = True)
            print('TOP50接口入向流量排名：')
            i = 0
            for each in temp:
                if i < 50:
                    print('%-30s%-35s%dbps' %(each[0],each[1][0],each[1][1]))
                    i += 1
                else:
                    break
        elif a == 2:
            temp = sorted(dict1.items(),key = lambda x:x[1][2],reverse = True)
            print('TOP50接口入向包量排名')
            i = 0
            for each in temp:
                if i < 50:
                    print('%-30s%-35s%dpps' %(each[0],each[1][0],each[1][2]))
                    i += 1
                else:
                    break
        elif a ==3:
            temp = sorted(dict1.items(),key = lambda x:x[1][3],reverse = True)
            print('TOP50接口出向流量排名')
            i = 0
            for each in temp:
                if i <50:
                    print('%-30s%-35s%dbps' %(each[0],each[1][0],each[1][3]))
                    i += 1
                else:
                    break
        elif a == 4:
            temp = sorted(dict1.items(),key = lambda x:x[1][4],reverse = True)
            print('TOP50接口出向包量排名')
            i = 0
            for each in temp:
                if i < 50:
                    print('%-30s%-35s%dpps' %(each[0],each[1][0],each[1][4]))
                    i+= 1
                else:
                    break
        else:
            print('输入有误！')

            

file = input('请输入文件名，请确保文件在本目录下，否则请使用绝对路径：')
sortpacket(file)
#update

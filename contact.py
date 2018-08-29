﻿print('|---欢迎进入通讯录程序---|')
print('|---0：查询所有人资料 ---|')
print('|---1：查询联系人资料 ---|')
print('|---2：插入新的联系人 ---|')
print('|---3：删除已有联系人 ---|')
print('|---4：退出通讯录程序 ---|')
import pickle
f = open('联系人.pkl','rb')
contact = pickle.load(f)
f.close()
while(1):
     number = input('请输入相关指令代码:')
     if number == '4':
          break
     elif number == '1':
          name = input('请输入联系人姓名:')
          if name in contact:
                print(name,":",contact[name])
          else:
               print('你输入的用户不存在')
     elif number == '0':
          for user,values in contact.items():
               print(user,values)
     elif number == '2':
          name = input('请输入联系人姓名:')
          if name in contact:
               print(name,"已存在",end=' ')
               print(name,':',contact[name])
               if input('需要修改吗？Y/N')=='Y':
                    contact[name] = input('请输入用户电话号码：')
          else:
                contact[name] = input('请输入用户电话号码：')
     elif number == '3':
          name = input('请输入需要删除的联系人：')
          if name in contact:
               del(contact[name])
               print(name+'已经删除了')
          else:
               print('你输入的用户名不存在')
     else:
          print('你输入的指令有误！')
print('感谢使用通讯录')
f = open('联系人.pkl','wb')
pickle.dump(contact,f)
f.close()

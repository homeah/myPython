def palindrome(str):
     '蜜蜂酿蜂蜜；风扇能扇风 ；奶牛产牛奶 ；清水池里池水清；静泉山上山泉静；上海自来水来自海上； 雾锁山头山锁雾 ；天连水尾水连天 ；院满春光春满院；门盈喜气喜盈门。'
     length = len(str)
     temp_length = length // 2
     for each in range(temp_length):
          if str[each] == str[length-1]:
               flag = 0
               length -= 1
          else:
               flag = 1
               break
     if flag == 0:
          return 1
     else:
          return 0
while 1:
     str = input('请输入句回文；（退出按Q）')
     if str == 'Q':
          break
     if len(str)<3:
          print('请输入大于3个以上的字')
          continue
     if palindrome(str):
          print('你输入的是回文')
     else:
          print('你输入的不是回文')

               

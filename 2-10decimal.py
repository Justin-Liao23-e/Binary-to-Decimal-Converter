while True:
     abc = input('What do you want to convert?')
     if abc =='bye':
             break
     elif abc =='2-10':
             while True:
                     a = input('enter any binary number: ')
                     if a == 'end':
                             break
                     else:
                          if '.' in a:
                               for i in a:
                                    if i not in '10.':
                                         print("Please enter '0' or '1'!!!")
                                         break
                                    if a.count('.') >1 or a[0] == '.':
                                         print('No such numbers!!!')
                                         break
                               else:
                                    answer = []
                                    for index,i in enumerate(a):
                                         if a[index] =='.':
                                              c = len(a[0:index])-1
                                              for ic in range(0,index,1):
                                                   plus = int(a[ic])*(2**c)
                                                   answer.append(plus)
                                                   c -=1
                                              c2 = -1
                                              for ie in range(index+1,len(a),1):
                                                   plus2 = int(a[ie])*(2**c2)
                                                   answer.append(plus2)
                                                   c2 -=1
                                              print(sum(answer))
                                              break

                          else:
                               for i in a:
                                    if i not in '10':
                                         print("Please enter '0' or '1'!!!")
                                         break
                               else:
                                    answer = []
                                    c = len(a)-1
                                    for i in range(0,len(a),1):
                                         plus = int(a[i])*(2**c)
                                         answer.append(plus)
                                         c -=1
                                    print(sum(answer))
     elif abc =='10-2':
             while True:
                     a = input('enter any decimal number: ')
                     ans = []
                     if a == 'end':
                             break
                     else:
                          if '.' not in a:
                               for i in a:
                                    if i not in '1234567890':
                                         print('Please enter numbers!!!')
                                         break
                               else:
                                    while int(a)//2 !=0:
                                         b = int(a)%2
                                         a = int(a)//2
                                         ans.append(str(b))
                                    b = int(a)%2
                                    ans.append(str(b))
                                    for i in range(len(ans)-1,-1,-1):
                                         ans.append(ans[i])
                                    for j in range(len(ans)//2):
                                         del ans[0]
                                    ans1 = ''.join(ans)
                                    print(ans1)
                          elif a[0] == '0' and a[1] == '.':
                               for i in a:
                                    if i not in '1234567890.':
                                         print('Please enter numbers!!!')
                                         break
                                    if a.count('.') >1 or a[0] == '.':
                                                 print('No such numbers!!!')
                                                 break
                               else:
                                    q = input('How many digits do you require???')
                                    for qt in q:
                                         if qt not in '0123456789':
                                              print('Numbers Please!!!')
                                              break
                                    else:
                                         ans.append('0.')
                                         a = str(float(a)*2)
                                         ans.append(a[0])
                                         for i in range(int(q)-1):
                                              temp = []
                                              temp.append('0')
                                              for j in a:
                                                   temp.append(j)
                                              del temp[1]
                                              temp2 = ''.join(temp)
                                              a = str(float(temp2)*2)
                                              ans.append(a[0])
                                         ans1 = ''.join(ans)
                                         print(ans1)
                          elif a[0] == '1' and a[1] == '.':
                               for i in a:
                                    if i not in '1234567890.':
                                         print('Please enter numbers!!!')
                                         break
                                    if a.count('.') >1 or a[0] == '.':
                                                 print('No such numbers!!!')
                                                 break
                               for index,i in enumerate(a):
                                    if a[index] =='.':
                                              b = int(a[0:index])%2
                                              c = int(a[0:index])//2
                                              ans.append(str(b))
                                              while int(c)//2 !=0:
                                                   b = int(c)%2
                                                   c = int(c)//2
                                                   ans.append(str(b))
                                              b = int(c)%2
                                              ans.append(str(b))
                                         
                                              for i in range(len(ans)-1,-1,-1):
                                                   ans.append(ans[i])
                                              for j in range(len(ans)//2):
                                                   del ans[0]
                                              
                                              last = []
                                              q = input('How many digits do you require???')
                                              for qt in q:
                                                   if qt not in '0123456789':
                                                        print('Numbers Please!!!')
                                                        break
                                              else:
                                                   a = '0.'+ a[index+1:len(a)]
                                                   a = str(float(a)*2)
                                                   last.append(a[0])
                                                   for i in range(int(q)-1):
                                                        temp = []
                                                        temp.append('0')
                                                        for j in a:
                                                             temp.append(j)
                                                        del temp[1]
                                                        temp2 = ''.join(temp)
                                                        a = str(float(temp2)*2)
                                                        last.append(a[0])
                                                   for x in last:
                                                        ans.append(x)
                                                   del ans[0]
                                                   ans.insert(1,'.')

                                                   ans1 = ''.join(ans)
                                                   print(ans1)
                                                   break
                                         
                          elif '.' in a:
                               for i in a:
                                    if i not in '1234567890.':
                                         print('Please enter numbers!!!')
                                         break
                                    if a.count('.') >1 or a[0] == '.':
                                                 print('No such numbers!!!')
                                                 break
                               else:
                                    for index,i in enumerate(a):
                                         if a[index] =='.':
                                              b = int(a[0:index])%2
                                              c = int(a[0:index])//2
                                              ans.append(str(b))
                                              while int(c)//2 !=0:
                                                   b = int(c)%2
                                                   c = int(c)//2
                                                   ans.append(str(b))
                                              
                                              b = int(c)%2
                                              ans.append(str(b))
                                         
                                              for i in range(len(ans)-1,-1,-1):
                                                   ans.append(ans[i])
                                              for j in range(len(ans)//2):
                                                   del ans[0]
                                              
                                              last = []
                                              q = input('How many digits do you require???')
                                              for qt in q:
                                                   if qt not in '0123456789':
                                                        print('Numbers Please!!!')
                                                        break
                                              else:
                                                   ans.append('.')
                                                   a = '0.'+ a[index+1:len(a)]
                                                   a = str(float(a)*2)
                                                   last.append(a[0])
                                                   for i in range(int(q)-1):
                                                        temp = []
                                                        temp.append('0')
                                                        for j in a:
                                                             temp.append(j)
                                                        del temp[1]
                                                        temp2 = ''.join(temp)
                                                        a = str(float(temp2)*2)
                                                        last.append(a[0])
                                                   for x in last:
                                                        ans.append(x)
                                                   for d in range(0,index-1):
                                                        if ans[d] == '0':
                                                             del ans[0]
                                                        else:
                                                             break
                                                   ans1 = ''.join(ans)
                                                   print(ans1)
                                                   break
     else:
          print("Please enter '2-10' or '10-2'!!!")
                                                                               
                             


                                   

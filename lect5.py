# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 05:08:02 2022

@author: hamza
"""


#for loop

name='rama abdlrahman'
for i in name:
    print(i)

name=['rama','abdlrahman']
for i in name:
    print('hello',i)

for i in range(9):
    print(i)

for i in range(ord('A'),ord('Z')+1,1):
 if(i==ord('Z')):
     print(chr(i))
     break;
 print(chr(i) ,end=',')

#or
for i in range(ord('A'),ord('Z')+1,1):
 if(i!=ord('Z')):
     print(chr(i) ,end=',')
 else: 
     print(chr(i))

#or
empty_string_to_add_into=''
for i in range(ord('A'),ord('Z')+1):
  if(i!=ord('Z')):
    empty_string_to_add_into+=chr(i)+ ',' 
  else:
     empty_string_to_add_into+=chr(i)
print(empty_string_to_add_into)

#######################################333

#or
st=''
for i in range(ord('A'),ord('Z')+1):
     st+=chr(i)+','
st=st[:-1]#split last comma
print(st)
##########################################


item=''
for i in range(26):#num of alpha letters
  if ord('a')+i != ord('z'):
     item+=chr(ord('a')+i) + ','
  else:
     item+=chr(ord('a')+i)
print(item)
#########################################

numsloop=[90,30,30]
summ=0
for i in numsloop:
    summ+=i
print(summ)
# add them all then print



#add print ---> 90... add print---->120... add print---->150
numsloop=[90,30,30]
summ=0
for i in numsloop:
    summ+=i
    print(summ)
#########################################
numsloop1=[90,0,77,0,0,66,50]
summ1=0
for i in numsloop1:
    if i != 0 :
        summ1+=i
        print('**************** to show that 0 is skiped:   ', i)
print('the summmmm:', summ1)
#########################################

for i in range(len(numsloop1)):
    print('content of list without skiping 0 :',numsloop1[i]) #will print all content of list
 ########################################
ss=0
for i in range(len(numsloop1)):
    if numsloop1[i]==0:
        ss+=0
    else:
        ss+=numsloop1[i]
print('another sol :',ss)
#############################################

l=[10,20,30,40]
for x in l:
    if x ==30: continue# will go to loop again ,will not go to next lines
    
    print(x) #30  tis line will be skipped
    print(x*2)#30  tis line will be skipped
# 10 .. 10*2 ..    20 ..  20*2  !!!when 30 return to loop!!! ..40 ..  40*2

#####################################
print('**************************************')
for x in l:
    if x==30:break # 30 and all values after it will not be seen!!  goooo out of loooop
    print(x)
    print(x*2)

print('*****************skip 0 using continue*********************')


numsloop1=[90,0,77,0,0,66,50]
summ1=0
for i in numsloop1:
        summ1+=i 
        if i == 0 :continue
        print('**************** to show that 0 is skiped:   ', i)
print('the summmmm:', summ1)


########
print('****************for loop with dic**********************')
dicc={'name':'rama','age':'22','salary':'4000'}
for x in dicc:
    print(x)#will print only keys
    print(dicc[x])#print values

print('*********using function to print keys and values************')
print(dicc.items())
print('********or***********')
for x in dicc.items() :
    print(x)
print('****or**********')
for x,y in dicc.items():
    print('key:',x,',', 'value:', y)
    #################################################
    
print('** using else in for loop without if !!! **')

digits=[0,1,2]
for x in digits:
    print(x)
else:
    print('there is no items left !')

######################################################

"""
Python allows the else keyword to be
 used with the for and while loops too. T
 he else block appears after the body of the loop. 
 The statements in the else block will be executed after all 
 iterations are completed. The program exits the loop only after
 the else block is executed.
The else clause executes after the loop completes normally
"""

print('*************************')
for currentLetter in 'Hello world!': 
   print('The current letter is', currentLetter)
else:
   print('All letters were printed.')
"""
The simple example above printed all the letters
 in the Hello world! string. Because the loop iteration 
 completed normally, the else statement was also executed
 and the text All letters were printed. was printed to the 
 screen
"""
print('*************************')


for currentLetter in 'Hello world!': 
   print('The current letter is', currentLetter)
   if currentLetter == 'w':
       break
else:
   print('All letters were printed.')
"""
Notice how the for loop was terminated
 when the letter w was encountered. 
 Because the loop iteration wasn’t completed
 normally, the else statement wasn’t executed.
 """
 
 #################################################
 
print('**simple example**')
print('** search for not exist name**')
gradedic={'rama':'100','samer':'50','ruba':'80'}
for i in gradedic:
   if i=='rua':
        print(gradedic[i])
        break
   
else:
       print('name not found')
 
print('**search for exist name**')
for i in gradedic: 
   if i=='rama':
        print(gradedic[i])
        break
else:
       print('name not found')
       
       
       
       ##############################################
print('** other sol!**')
for x,y in gradedic.items():
   if x=='samer':
      print(x, ' grade is ', y)
      break#go out of loop so else not seen because its تابعة to for loop
else:print('not found')
 
 ################################################
 
 ## for previous question we can use . vales or .keys   or  .items   or nothing of them 
 

dic={"Name":"Hashem" , "Age":23 , "mark": 100}
for i in dic.values():
    if i == "Hashem":
        print(dic["mark"])
else:
    print("No values left")



dic={'mayas':90,'ruba':95,'rania':100,'alaa':77}
for i in dic.keys():
    if i=='rania':
        print(dic[i])
        break
else:
    print("the name not found")

 ###############################################
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 














































































































































   
    





































































       



































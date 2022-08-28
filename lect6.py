# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 18:36:31 2022

@author: hamza
"""

"""
****معادلة التدريب الجامعي
ai developer عادي بدون رياضيات  ****
"""
print('**while loop**')
n=10
i=1
summm=0
"""
(non stop!!)
while i<n:
    summm+=i
    print(summm) 
"""
##the right way 

while i<=n:
    summm+=i
    i+=1
    print(summm)
"""
1
3
6
10
15
21
28
36
45
"""
print(summm) ##print final sum

print(i)#print final i   i=11 which is not less than or equal 10 so stop عندها

###################################################
### we can use else with while
print('********')
while i<=n:
    summm+=i
    i+=1
else:
    print(i)
print(summm)
#####################################################
#space in python like {} in other languages
#####################################################
### decleration ###
n=10
o=1

print('********')
while o<n:
    print(o)
    o+=1
print('out of range')
print(o)

######################################################
print('**infinite loop**')
"""
flag=1
while flag:
    print('r')
    
    """
    
    #################################################
    
"""
userin=int(input('enter a number'))
while userin in range(-30,30):
      
    if userin>0:
        print('its pos+ num')
        break
    elif userin==0:
        print('its zero')
        break
       
    else:
        print('its neg-')
        break
"""
#####################################################
"""
i=1
while ++i<=5:
    inp=int(input('enter number'))
    if inp>0:
        print('its pos+')
    elif inp==0:
        print('its zero')
    else:
        print('its neg-')
    i+=1
"""
#######################################################
"""
i=1
while  ++i<= 1:
    inp1=input('enter yes or no:   ')
    if inp1=='yes':continue
        
    else:
       print('bye')
       break
i+=1
"""
#######################################################
"""
a='yes'
while a=='yes': 
    na=input('enter your name')
    print(na)
    a= input('enter yes to cont or no to stop')
else:
    print('thanks')
"""
#######################################################

print('**functions in pyth**')

def func_name(x):
    print(x)

func_name(66)
func_name('roro')
func_name(22.3434)
#can ues same function aand for different datatypes!!


def fun1(n):
    print('hello', n)
fun1('mariam')

"""

def fun2():
    x=int(input('num1:'))
    y=int(input('num2:'))
    print(x*y)
fun2()
"""
#****************using return shold be called inside print*************
"""
def fun2():
    x=int(input(' num1:'))
    y=int(input('num2:'))
    return x*y
#any line after return not seen , no error given but not allowed to write here
    print('roro')#not seen
print(fun2())
"""
#*****************we can return any thing **********************
def fun2():
    return 'rama',80
print(fun2())
#************************************




















































































































































































































































































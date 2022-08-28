# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 03:22:22 2022

@author: hamza
"""
"""
Task1
"""
"""
dic = {"Khaled":50,"Mouhamed":90,"Ahmed":70,"welcome":20}


#copy element from the origenal dictionary to new one
new = dic.copy()
print("The Origenal:", dic)
print("The new one :", new)
print("**************************")
"""



"""
#get the value by using the key and 
print("The value of the key Khaled",dic.get("Khaled"))

#you can declear value dose not exseist and give it avalue but it will not tkae it in dictionary 
print("ammer",dic.get("ammer",77)) 
print("**************************")

"""

"""
#popitem delete last element in the dic key and the value  

result=dic.popitem()
print(result)
print(dic.items())
print("**************************")
"""
"""
#pop give any value and deldet the last iteme
value=dic.pop("Ahmed")
print("the value of Ahmaed is ",value)
print(dic)
print("**************************")
"""

"""
#update updating the data and it add the element to the last place
d={"sameer":99}

dic.update(d)
"""
"""
print(dic.items())
print("**************************")
"""

"""
#give all keys same value
key=['a','b','c','d']
value2=80
new = dic.fromkeys(key,value2)
print("The Origenal dictionary :",dic)
print("The new one :",new)
print("**************************")

"""

"""
#clear it clear the content of dic but it still exest 

dic.clear()
"""
"""

#string function
x = "12354785669854412503665"
x.split("5") #بفصل عند كل 5 بشوفها
#--------------------------------------------
friends='mayas and ruba and ola'
friends.partition("and")#اول كلمة اند من الشمال بحطها لحال و ما قبلها لحاله و ما بعدها لحاله
friends.rpartition('and')#اول اند من اليمين ....
#---------------------------------------------
a='he is a good man but he is liar'
a.find('is') # اندكس 3 بتبلش من اندكس 3
a.rfind('is')#اول از من اليمين بشوف من اي اندكس بتبلش الكلمة 
#---------------------------------------------
a.index('g')# هل السترنج يحتوي على انكس قيمته حرف جي
#----------------------------------------------
a.replace ('g','i')
#----------------------------------------------
a.count('i') #كم مرة تكررت
#----------------------------------------------
name='mAyas masalmeh'
name.capitalize()# اول حرف كبتل
name.title()#اول حرف من كل كلمة كبتل
name.upper()
name.lower()
name.swapcase()
name.center(30)#بضيف فراغات يمين شمال السترنج حتى يصير عدد الاندكس مساوي للعدد الي بين القوسين 
name.ljust(60) # بخلي السترنج على جهة اللفت و جهة اليمين بعبيها فراغات لحتى يوصل لغدد الاندكس الي بين القوسين
name.rjust(50)# بخلي النص على جهة اليمين و على الشمال بضيف فراغات 
'435'.zfill(10) #0000000435 بطبع:
#-------------------------------------------------
color='redblue'
color.isalpha()
color.isupper()
color.islower()
color.istitle()
color.isascii()
color.isspace()#غلط لانه مو فاضي
y='1234565'
y.isalnum()#T
y.isdecimal()#T
y.isdigit()
y.isnumeric()
#-----------------------------------------------------
course='      machine learning        '
course.strip()#بقص الفراغات من الطرفين 
course.rstrip()
course.lstrip()
#------------------------------------------------------
"""


#lang = """ python,
#c++,
#c """
#lang.splitlines()
#------------------------------------------------------

"""
animals="dog"
animals.startswith("p")
animals.endswith('g')
#------------------------------------------------------
numbers=','.join( ('one', 'two', 'three') )
print(numbers)# one,two,three
hi='  '.join('hello') # h e l l o
print(hi)
#------------------------------------------------------
import numpy as np
pi="The value of pi is {}".format(np.pi)
print(pi)  #The......is 3.14
color='{0} and {1}'.format('red', 'blue')
print(color)# red and blue
steps="First: {first},Last: {last}.".format(last='Z', first='A')
print(steps)  #First:A,Last:Z
#---------------------------------------------------------
print(steps._len_())
print(steps._add_('hello'))


"""
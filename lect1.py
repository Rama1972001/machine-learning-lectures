# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
@author: rama
Created on Mon Aug 15 19:10 2022
"""
# string can be printed in single or double '' or""
print()


#shift+tab in jupetar
#عشان اشوف الخيارات الممكنة ctrl+space

#each one of print statments on a line because there is a semicolon
print("rama");print(21);

# ** power, * multi, // return just int 7//3=2

#no need to determine datatype in python


#var
x=50;
x='roro'
#can use same variable and update value and update also datatype!!
name="rama"
active=True;
print(type(x))  # its str
###########################################

#casting
##########################
names="rama","rua" #tuple
data=(999,90.987, False,'roro')#can include different datatypes
print(data)

print(data[0])#index 0 is 999
###########################################
#in tuple there is no update no delete no insert just save data 
####data[0]=40
###typeError: 'tuple' object does not support item assignment
#######################################3####


#List
namesList=['rana',60,True]
print(names)
namesList.append('rama')
#append,extend,insert  to add
# append add one item or more at last index in list 
namesList.append(['ali','alaa']) #will be added to the end of the list 
#list of list


# to select ali:
    
print(namesList[4][0]) #will give ali - list of list-


#extend will add many values at end of list  not as list of list but each index alone
namesList.extend([50,90,9999,'dana'])
print(namesList)

#insert

namesList.insert(3, 'ameer') #change index 3 to ameer
#namesList.clear()  clear all content of the list 
#namesList.pop(0) clear specific index
#namesList.remove('rana') clear specific content 
























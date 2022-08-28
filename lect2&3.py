# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 20:40:11 2022

@author: hamza
"""
family1=('ali','sameer', 'ahmad')
f2=('rana','rami','mousa')
f3=('momd','safa','dana')
f4=('ruba','ali','emad')

home1=(family1,f2)
home2=(f3,f4)
print(home1[1][2])#print mousa


#nested loop to print all names first loop on families then loop on names in each family





#dictionary

#key :   values
#key not only str can be any datatype
dic={ 'name':'ruba'  ,  'age':21    ,    'salary':9000   ,     70:'sameer'  }
#select values using the key
print (dic['name'])
print(dic.keys())#show all keys
print(dic.values())#show all values
print(dic.items()) #show all dic


#var using set 
nums=[30,40,50,60,80,80]
v=set(nums)
print(v)

# لا يوجد تكرار بال set 
#الترتيب عشوائي داخلها كل ما اعمل رن بتغير 

#  بقدر اضيف و اعدل عليها



n=('roro','soso')#this tuple will be added to set  v
v.update(n)
print(v)

#بما انه الترتيب عشوائي ما بقدر اضيف او احذف من اندكس معينه فقط بقد لقيمة معينة 
v.add('Ya Rab')
print (v)
#v.remove('Ya Rab') اذا  القيمة مو موجودة بعطي ايرور
#v.discard('Ya Rab') اذا القيمة مو موجودة ما بعطي ايرور لذلك استخدامه افضل 
############################################
#اذا انت حطيت ارقام متسلسلة لا يتغير ترتيب الset
l=[1,2,3,4]
s=set(l)
print(s)
############################################

#search
my_name='rama abdlrahman'
print('k' in my_name) 
print('r' in my_name )

#############################################

#search using in used  in tuple, set , list
print('ruba' in nums)
#del
del(s) #delete from memory

print(len(v)) #return count -size-
# len=8   0-7


##############################################33

#casting

number=9
print('my num is :'  + str(number))
print(type(number))#datatype still int


num2='99'
num1=int(num2) 


# aall numbers when casting are true just empty things false
d=0#print false 
d1=-1
d2=70
d3=""
d4=" "#not empty there is a space  trueeee
d5=[]

print(bool(d5))


c='a'
#get asci code 
print(ord(c))
c=" "
print(ord(c))

c=65
print(chr(c))
####################################################

#var range
r= range(0,7,1)#start from 0, to 7, step =1
print(r[0],r[1],r[3],r[2],r[4],r[5], r[6])



r= range(2,7,2)
print(r[0],r[1],r[2])

r=range(24,0,-2)
print(r[0],r[1],r[3],r[2],r[4],r[5], r[6], r[11])

#range take only int so we use ord to take str characters
#from A to Z and use Z+1 To let Z in because Z in normal not in
r=range(ord('A'),ord('Z')+1,1)
print(r[0])
print(chr(r[0]))
print(r)
print(chr(r[0]),chr(r[25]))

#DIC.FROMKEYS() نعطي اكثر من كي فاليو وحدة


#enter statment

####x=input("plz enter name")
####print('hi', x)
#print just take string

###x=int(input("plz enter num"))
###print(100* x)

################################################


#string split
name1="rama abdlrahman"
print(name1[0:5]) #4 indexes 0-4
print(name1[0:3]) #2 indexes 0-2
print(name1[0:2]) #1 indexes 0-1
print(name1[0:]) #start from 0 to end

print(name1[:]) #start from first to end
print(name1[4:11]) 
print(name1[4:-1]) #لحتى قبل الاخير بواحد
print(name1[4:len(name1)]) #from 4 to end

ls=[3,4,9,8]
#   0 1 2 3
x=ls[1:3] #2 indexes  0 1 2 without 0 because it start from 1
print(x)#   4,9




###################################################

names="Rama,rua,hoho,meme,ranosh,soso" #this is a string ... we will convert it to list
n=names.split(",")
print(n)

#split just on the first comma

names="Rama,rua,hoho,meme,ranosh,soso" #this is a string ... we will convert it to list
k=names.split(",", 1)
print(k)
#split just on the first 2 commas

names="Rama,rua,hoho,meme,ranosh,soso" #this is a string ... we will convert it to list
k=names.split(",", 2)
print(k)


##################################################

i='sami and fadi'
j=i[1:4]
print(j[::-1])  #inverse


###############################

#افصلي على اساس الفاصلة بس صفر مرة ولا مرة 
word='sasa,soso,sisi'
print(word.split(',', 0))

###############################










































































































































































































































 
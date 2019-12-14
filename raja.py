''''
a=100
if a>100:
    print ("a is greater than 100")
elif a==100:
    print ('a equal to 100')
else:
    print ('a is less than 100')'''


#next program
'''
a=[1,2,3,4,5]
for i in a:
    print (i)'''


#next program
'''
a=[4,9,6,8]
for i in a:
    print (i)'''

#next program

'''a=[1,2,3,4,9,6,8]
for i in range (0,len(a)):
    a[i]=a[i]+2


print (a)'''

#next program

'''a=[100,200,300,400]
count=0
for i in a:
    count=count+1

    print (count)'''

#next program

'''a=[100,200,300,400]
sum=0
for i in a:
    sum=sum+i
    print (sum)'''


#next program

'''a=[6,9,8,10,9,8,6,9]
b=8
count=0
for i in a:
    if i==b:
        count=count+1
        print (i)'''
    
    
#next program
'''a=[6,9,8,10,9,8,6,9]
maxvalue= a[0]

for i in a:
    if maxvalue < i:
        ma9xvalue = i

        print (maxvalue)'''

#next program - count 


'''a=[34,56,88]
count=0

for i in a:
    count = count+1
    print (count)'''

'''a=43
if a==34:
    print ("yes")
elif a>34:
    print ("no")'''


#next program: maxvalue example

'''a=[1,4,9,8,96,1,4,4]
maxvalue=a[0]
for i in a:
    if maxvalue < i:
        maxvalue = i
        
print (maxvalue)'''


#next program - type of sum

'''a=[1,4,9,8,'raja',96,1,4,4]
sum=0
for i in a:
    if type (i)==int:
        sum=sum+i
print (sum)'''

#next program ---own program---

'''username="admin"
password="cisco123"

for i in username:
    username=input ('enter username:')
    password=input ('enter password:')
    if username =="admin" and password == "cisco123":
        print ("allow")
    else:
        print ("deny")'''

#next program - diff between sum of sqr and sqr of sum example

'''a=int (input("enter the number"))
sum,sum1=0,0
for i in range(1,a+1):
    sum=sum+i**2
    sum1=sum1+i
print (abs (sum-sum1**2))'''


#next program - alpha numeric

'''a='adafafdaf1213@@@'

for i in a:
    if i.isalpha():
        print (i)'''
    
    


#next program - factorial example
'''a=int (input('enter the value'))
sum=1
for i in range (1,a+1):
    sum=sum*i
print (sum)'''

#next program -welcome to python
'''
training=input ('enter course')
name=input('enter name')
print ('hi',name, 'welcome to', training)
                
print ('hi {} welcome to ()'.format ('name,course'))'''

#next program
'''
while True:
    command=input ('enter statement:')
    if command=='start':
        print ('car started')
    elif command=='stop':
        print ('car stopped')
    elif command=='exit':
        break
    else:
        print ('dont understand the command')'''


'''a=10
while True:
    a-=1
    print(a)'''


# next program -  loop program - while True


 
'''febonaxi serias try'''


# next program


'''name=input('your name:')
weight=int (input('your weight:'))
KL=input('weight in K or L:').lower()

if KL=='k':
    convert=weight*2.2
    print (name, 'ur weight in kg', convert)
elif KL=='l':
    convert=weight*2.2046226218
    print (name, 'ur weight in pounds',convert)
else:
    print ('invalid')'''


#next program

'''name=input('your name:')
Height=int(input('your height:')
minch=input('your height in cm or inch:').lower

if cminch=='cm':
           convert=height*30.48
           print (name, 'your height is in cm',convert)
elif cminch=='inch':
    convert=height*2.54
    print (name,'is your height in inches',convert)'''
    
    

#next program

'''mailid=input('enter email id:')
split=''
for i in mailid:
    if i=='@':
        break
    split=i
    print (split,end='')'''


#next program

'''a='adafafdaf1213@@@'

for i in a:
    if i.isalpha():
        print (i,end='')'''


#next program - slicing

'''
a="raja academy"

#print (a[0:4])
#print (a[-len(a):])  ----- to find a value among large data. 'a' considered lard data

#print (a[0:12:2])  ----->>> slice two after two'''

#next program

'''a='abcd'
b=int(input('enter the number:'))

print (a[b:]+a[0:b])   ---->>>> enter the number and you get the value'''
#print (a[2:]+a[0:2])
#print (a[3:]+a[0:3])
#print (a[slicing:]+a[:slicing])

#next program -  palindrome

'''a=input('enter the palindrome:')    
if a[::-1]==a:
    print ('is palindrome')

else:
    print ('not palindrome') '''


#next program - leap year

'''a=int(input('enter the year:'))
    
if a%4==0:
    if a%100==0:
        if a%400==0:
            print ('leap year')
        else:
            print ('not leap year')
    else:
        print ('is leap year')
else:
    print ('not leap year')'''


#next program - if and else ---practice

'''a=int(input('enter the age:'))

if 0<a<=10:
    print ('children')
elif 10<a<=20:
    print ('youth')
elif 20<a<=40:
    print ('middle')
elif 40<a:
    print ('old man')
else:
    print ('invalid age')'''


#next program

'''50%-60% >>>> night and evening
60%-70% >>>> evening ---good or bad --->>> assingment and even
70%-80% >>>> assignment

write a program.'''

'''i=1
count =1
val = "access-list ACL_INSIDE3502 extended deny ip 123.123.{}.{} 255.255.255.255 125.125.125.125 255.255.255.255"
while i < 255:
              j=1
              while j < 255:
                             count +=1
                             newval = val.format(str(i),str(j))
                             print(newval)
                             j += 1
              i += 1
              if count > 1:
                             break'''



#next program

'''age=int(input('enter age:'))

if age<=10:
    print ('child')
elif 10<age<=25:
    if age<18:
        print ('school')
    else:
        print ('college')
elif 25<=age<60:
    if age<=40:
        print ('employee')
    elif 40<age<50:
        print ('manager')
    else:
        print ('vrs')
else:
    print ('senior citizen')'''

#next program - leap year

'''a=int(input('enter year:'))

if a%4==0:
    if a%100==0:
        if a%400==0:
            print ('leap year1')
        else:
            print ('not a leap year1')
    else:
        print ('leap year2')

else:
    print ('not a leap year2')'''

#next program


'''a=[10,15,12,30,11]
maxvalue=a[0]

for i in a:
    if maxvalue<i:
        maxvalue=i
print (maxvalue)'''

#next program - sum

'''a=[10,15,12,30,11]
sum=0

for i in a:
    sum+=i   #we can replace sum=sum+i or sum+=i
    
print (sum)'''

#next program - count


'''a=[10,15,12,30,11]
count=0

for i in a:
    count+=1  #we can replace count+=1 or count=count+1
print (count)'''

#next program - repeater

'''a=[3,3,3,5,7,3,5,7,7,8,8,3]
count=0
b=int(input('enter the number:'))
for i in a:
    if i==b:
        count=count+1 #we can replace count=count+1 or count+=1
print (count)'''

#excercise:-

'''a=[1,2,3,4,'str']'''  #i need only interger to be printed. if there is str reject and add
'''a='rajasubramani@cisco.com''' #i need after @ and before @
            

'''a='abcd'
b=int(input('enter the number:'))

print (a[b:]+a[0:b])'''


#next program:-


'''a=('bita academy')'''

#print (a.upper())  (or) a.isupper() -->> true or false
#print (a.lower())
#print (a.capitalize())
#print (a.casefold())
#print (a.title())
#print (a.swapcase())
#print (a.center(30))
#print (a.find('academy'))
#print (a.replace('bita', 'tata'))

#next program -  alpha numb

'''a='ab123-#$96cd1'

#get only alpha
for i in a:
    if i.isalpha():  
        print (i,end='')

#get only special char

for i in a:
    if not i.isalnum():
        print (i,end='')'''

#next program --->>> split

'''a='bita academy'

a=a.split ()
print (a)'''

#next program --->>> join the list

'''a=['b','i','t','a']
a=''.join(a)
print (a)'''

'''a=['ba','hu','ba','li'] 
a='/'.join(a) ----------->>>> what '/' you give inside the string will be sort in output
print (a)'''

#next program. -->> convert str to var

'''a=['10','20','30']
for i in range (len(a)):
    a[i]=int(a[i])
print (a)'''

#+++++++++++++++++++++++++++++++++
       #TUPLE and Set
#+++++++++++++++++++++++++++++++++

# next program

'''a=[10,20,30]
b=tuple(a)
print(b)
print (b.count(10))'''

#next program

'''set1={1,2,3,4,5,7}
set2={5,8,3,5,6}'''

#print (set1|set2) #--->>> write sequence
#print (set1&set2)  #--->> common in both set1 and set2
#print (set1-set2)   #---->>> Minus set1 to set2


#++++++++++++++++++++++++++++++++++++++++++++
              #Dictionary
#+++++++++++++++++++++++++++++++++++++++++++

'''dict={'a':'apple','b':'ball','c':'correct'}
print (dict['a'])
print (dict['b'])
print (dict['c'])'''

'''dict={'count':{'india':['chennai','madurai']}}
print (dict['count']['india'][1])'''
                
#++++++++++++++++++++++++++++++++++++++++++++++++++

#next program -->> Return

'''def add(a,b):
    c=a+b
    return c     #program will not run after return command. by default
print (add(10,20))'''

'''def add(a,b):
    c=a+b
    print (c)'''  #for example match both program you can find the difference


#next program - palindrome different method using return fuctions

'''def palindrome(a):
    a=a.lower()
    if a==a[::-1]:
        print ('palindrome')
    else:
        print ('not')

palindrome('malayalam')'''


#next program - how to use fuctions with factorial "def function"

'''def fact(a):
    
    sum=1
    for i in range (1,a+1):
        sum=sum*i
    print (sum)

fact(5)'''

#+++++++++++++++++++++++++++++++++++++++++++
#     how to use import
#++++++++++++++++++++++++++++++++++++++++++++







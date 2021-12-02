# import pandas as pd
# import numpy as np
# # data_set={
# #     'vehicle':['car','schooter','bike'],
# #     'tyre' : [4,2,2]
# # }
# # v = {'Name': ['Tom', 'nick', 'krish', 'jack'], 'Age': [20, 21, 19, 18]}
# # v=['asurn','trisuran','karthik']
# # df=pd.DataFrame(v)
# # print(df)
#
# # data=np.array([1,2,3,4,5])
# data=np.array(['kliran','matran','aaran'])
# ser=pd.Series(data)
# print(ser)
#
#
# l='striide'
# print(l.count('d'))
#
# lst = [1,3,5,2,6,2,3,1,4,5,1]
#
# dic = {x:lst.count(x) for x in lst}
#
# print(dic)
#
#

a='hello world'
k=len(a)-1
while k>0:
    print(a[k])
    k=k-1



x = 77

def foo():
    global x
    x=5555+x
    print(x)
    x = 99
    print(x)
foo()
# print(x)
l1=[1,2,3,3,4,5,9]

# d=78
# s=d
# print(id(s))
# print(id(d))

# for x in range(0,len(l),2):
#     if l[x+1:]:
#      d[l[x]]=l[x+1]
#     else:
#      d[l[x]]=0
# print(d)

# dict={l[x]:l[x+1] if l[x+1:] else l[x]=0 for x in range(0,len(l),2)}
# print(dict)


def outer():
    x = 190

    def inner():
        nonlocal x
        x = 10+x
        print("inner:", x)

    print("outer:", x)
    return inner()

f=outer()





def smart_div(func):
    def inner(a,b):
        if b==0:
            print("sorry",b, "is not divisible by",a)
        else:
            return func(a,b)
    return inner
#
#
@smart_div
def div(a,b):
    return a/b
print(div(4,0))


# y=[1,7,5,6,8,3,9,2,7,33]
# x=y[0]
# print(x)
# for i in y:
#     if i>x:
#         x=i
# print(x)

# for x in range(len(y)):
#     for j in range(x+1,len(y)):
#         if y[x]>y[j]:
#             y[x],y[j]=y[j],y[x]
# print(y)
#
for i in range(5,1,-1):
    print('executed')
#
#
# palindrome number
# word=input("enter the word",)
# if (word==''.join(reversed(word))):
#  print("it is a palindrome")
# else:
#      print("not a palindrome")


l=[1,2,3,5,67]
d={}
for x in range(0,len(l),2):
   if l[x+1:]:
    d[l[x]]=l[x+1]
   else:
    d[l[x]]=None
print(d)


# prime  number
# lower=input("enter the lowest number, ")
# higher=input("enter the higher number, ")
num=6
for i in range(0,num):
    if i>1:
        for x in range(2,num):
            if i%x==0:
                break
    else:
        print(i)


# checking single number is prime or not
def isprime(n):
# for x in range(0,6):
 if n>1:
    for i in range(2,n):
        if n%i==0:
            return False
    return True
 else:
    print('please check the number')

print(isprime(10))



# def extendList(val, list=[1,2,3]):
#     list.append(val)
#     return list
#
#
# # list1 = extendList(10)
# # print("list1 = %s" % list1)
# list2 = extendList(123, )
# # list3 = extendList('a')
# print("list1 = %s" % list1)
# print("list2 = %s" % list2)
# print("list3 = %s" % list3)

# a = ["RCB", "KKR", "CSK", "MUM"]
# f = []
# for x in range(len(a)):
#     if a[x + 1:]:
#         f.append(a[x] + " vs " + a[x + 1])
#     else:
#         f.append(a[x] + " vs " + a[0])
#
# print(f)


a = ["RCB", "KKR", "CSK", "MUM"]
f = []
for x in range(len(a)):
    if a[x+1:]:
      f.append(a[x]+'vs'+a[x+1])
    else:
        f.append(a[x]+'vs'+a[0])
print(f)


# d1={1:2,3:4}
# d2={7:9,5:9}
# d3={0:2,9:3}
# d1.update(d2)

# import csv
# with open('txtfile.csv','w',newline='')as f:
#     w=csv.writer(f)
#     w.writerow(['no','name','address'])
#     n=int(input('enter the details'))
#     for i in range(n):
#         no=int(input('enter the number'))
#         name=input('enter the name')
#         address=input('enter the address')
#         w.writerow([no,name,address])
# print('the file data written to file successfully' )
#
# ----to read data from csv file
# f=open('txtfile.csv','r')
# r=csv.reader(f)
# data=list(r)
# print(data)

# f=open('rest.txt','a+')
# f.write('thanks\n')
# # f.write('this is charan')
# f.close()
# print('file was created successfuly')

# f=open('emp.txt','r')
# data=f.readlines()
# print(data)

s1=[4,6,7]
print(s1.pop())
print(s1)
print(s1.pop())


k='animal'
s=set(k)
v={'a','e','i','o','u'}
c=s.intersection(v)
print(c)

list=[1,2,3,5]
print(list)
print(list.clear())
print(list)

s='thanks'
print(s)



d={1:2,3:4}
print(d)
del d[1]
print(d)

set1={1,2,3,4}
set1.add(77)
print(set1)




d={'kiran':100,'charan':200,'madan':100}
dict={}
temp=[]
for key, value in d.items():
    if value not in temp:
        temp.append(value)
        dict[key]=value
print(dict)


list1=[1,2,3]
list2=[4,5,6]
k=[list1[x]+list2[x] for x in range(len(list1))]
print(k)


k=['red','black','white','green']
l=[]
for i in range(len(k)):
     if k[i+1:]:
      l.append(k[i]+ 'versus' +k[i+1])
     else:
         l.append(k[0]+'match'+k[i])
print(l)




# dict={}
# for x in d:
#     if x not in dict.keys():
#         dict[x]=1
#     else:
#         dict[x]=dict[x]+1
# for key,value in dict.items():
#     print(key,'occyred',value,'times')
#
# d={'kiran':100,'charan':200,'kiran':500}
# for key,val in d.items():
#

class Depress:
    def __init__(self):
        self.name='kiran'
        self.roll_num=67
    def method1(self):
        print('name is ',self.name)
        print('num is ', self.roll_num)
obj=Depress()
obj.method1()


class Father:
    def m1(self):
        print('loved')
class Child(Father):
    def m2(self):
        print('childmetgod')
c=Child()
c.m1()
c.m2()

# t='madam'
# s=''
# for x in t:
#     s=x+''+s
# if s==t:
#     print('string s palindrome')
# else:
#     print('string is not a palindrome')

l=[1,2,3,4,5,6]
for i in range(0,len(l)):
    for j in range(i,len(l)):
      print(i,j)






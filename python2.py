word=input("enter the word:")
# d={}
# for x in word:
#   if x not in d.keys():
#      d[x]=1
#   else:
#       d[x]=d[x]+1
# for k,v in d.items():
#      print(k,"occured", v, "times")


#removing duplicate values in dict
dic={1:"charan", 2:"kiran", 3:"charan"}
d={}
temp=[]
for key,value in dic.items():
    if value not in temp:
        temp.append(value)
        d[key]=value
print(d)

dic = {1: "charan", 2: "kiran", 3: "charan"}
print(dic)
f = {key: value for key, value in dic.items()}
print(f)
d = {value: key for key, value in f.items()}
print(d)

dict1={1:2, 3:4}
dict2={5:6, 7:8}
dict1.update(dict2)
print(dict1)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
l=[list1[x]+list2[x]for x in range(len(list1))]
print(l)
l = []
for x in range(len(list1)):
    print((list1[x] + list2[x]))

import functools
import operator

li = [[14], [215, 383, 87], [298], [374, [2, 5]], [2, 3, 4, 5, 6, 7]]
flat_list = functools.reduce(operator.concat, li)
print(flat_list)

# matrix = [[0, 1, 2, 3, 4],5,6,7,8,[0, 1, 2, 3, 4],9,10,11,[0, 1, 2, 3, 4],12,13,14,[0, 1, [45,7,8,9],2, 3, 4]]


list = ["kiran", "charan", "madan"]
# o/p=[k,c,m]
list = ["pen", "gun", "bun"]
upper = [x.upper() for x in list]
print(upper)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
# d={list1[x]:list2[x]for x in range(len(list1))}

print(dict(zip(list1, list2)))
print("successfull")

# list=["pink", "green", "blue"]
# o/p=["p","g","b"]

l = [x[0] for x in list]
print(l)

l = ["orange", "grapes", "banana"]
l.sort()
print(l)

# --------1.nested to flat
# res=[[2,6],[4,6],4,[7,8],[9,0]]
# l=[]
# for x in res:
#     if type(x) is list:
#         l.extend(x)
#     else:
#         l.append(x)
# print(l)

# -------sorting the elements accoring to order

# 20-10+10-5+5
# def func(num):
#     s = 0
#     for i in str(num):
#         s+=int(i)
#     if len(str(s))==1:
#         print(s)
#     else:
#         func(s)
# func(20)


# 789-7+8+9-
# 24-2+4-6


# converting from nested list to flatten the list
# num=[[34],2,3,4,[8,9,0]]
a=[]
# def func(num):
#  for ele in num:
#      if type(ele)!=list:
#       a.append(ele)
#      else:
#       func(ele)
#      return a
# num=[[34],2,3,4,[8,9,0]]
# print(func(num))



temp=[1,5,3,2,5,1,4,5,9,0,8,9,8,8]
# 1, 4, 7,10,12
k=[]
res=[x for x in range(len(temp)) if temp[x]==8][1]
print(res)

word="prudhvi"

print(len(word))

r = [1, 4, 5]

v = [r.append(x) for x in range(10)]
print(r)



# l=[1,2,3,4,5]
# def doubleIt(x):
#   return 2*x
# l1=list(map(doubleIt,l))
# print(l1)

# Removing duplicates values by another merthod(dict comprehensiomn)
# d={1:2, 3:2,4:5}
# dict={val:key for key, val in d.items()}
# v={key:val for val, key in dict.items()}
# print(v)


# nested fun:
def outer():
    print("this is the outer func")

    def inner():
        print("this is the inner functiom")
    return(inner)
f1=outer()
f1()

def probs(a,b):
  sum=a+b
  mul=a*b
  return sum, mul
print(probs(3,4))


# program to display the right angled triangle
# n=int(input("enter the num of rows:"))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# for i in range(4):
#   for j in range(4):
#        print("i=",i," j=",j)
#   print()


l=[2,3,8]
print(l)
(l.remove(8))
print(l)
d={1:2, 2:3}
print(d)
print(d.pop(1))
print(d)

def decor(func):
    def inner(name):
        if name=="kiran":
            print("hi this is" , name, "bad")
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("Hi this is ",name)
wish("charan")
wish("kiran")



def smart_div(func):
    def inner(a,b):
        if b==0:
            print("sorry",b, "is not divisible by",a)
        else:
            return func(a,b)
    return inner
#
#
# @smart_div
# def div(a,b):
#     return a/b
# print(div(4,5))
# print(div(3,0))

from random import *

for i in range(7):
    for j in range(0,9):
        print((8-i),end=" ")
    print()

for k in range(5):
    for l in range(1,6):
       print((6-l),sep=" ", end=" ")
    print()

n=5
for i in range(n):
    s=str(n - i)+" "
    print(str(s)*5,sep="")

string = 'geeks'
length = 17

# If no fill character is provided, space
# is used as fill character
print(string.rjust(length))

# how to remove the dup val in dict
n=5
for i in range(n):
  if i ==0 or i ==4:
       print('* '*5)
  else:
       print('* '.ljust(8))


def gen(num):
    while num>0:
        yield num
        num=num-1
val=(gen(5))
for x in val:
    print(x)


# remove the nested list
#
k=[]
def func(num):
  for ele in num:
      if type(ele)!=list:
       a.append(ele)
      else:
       func(ele)
  return a
num=[[34],2,3,4,[8,9,0]]
print(func(num))
# global  key word
# global key word is used for two purposes
# 1-to use the global var inside the func
# 2-to make global variable availble to the func so that req modifications can be done



# n=int(input("enter some num = ",))
# temp=n
# rev=0
# while n>0:
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if rev==temp:
#     print("the num is palindrome")
# else:
#     print("the num is not palindrome")


# s="hello how are you"
# k=s.split()
# print(k)
# l=k[::-1]
# print(l)
# for x in l:
#     m=m+" "+x
# print(m)
#

s="hello world"
k=s.split()
# print(k)
p=""
t=k[1][::-1]
# print(t)
k[1]=t
# print(k)
for x in k:
    p=p+" "+x
print(p)



def myfunc1():
    y = 'charan'
    def inner():
        nonlocal y
        y = 'raju'
        print(y)
    print (y)
    return inner
f=myfunc1()
f()



l1 = [1,2,3,4,5,6,7,8,9]
print(l1[-5:])





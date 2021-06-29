a=10
# # def func():
# #     a=444
# #     print(a)
# # def func2():
# #
# #     print(a)
# #
# # func()
# # func2()
# #
# #
# # n=12
# # def glob():
# #     global n
# #     n=45
# #     print(n)
# # def glob2():
# #     print(n)
# # glob()
# # glob2()
# #
# #
# # f=open("docfiles.txt",'r')
# # print(f.read())
# #
# #
# #
# #
# #
# # from random import*
# # # for i in range(10):
# # #     print(randint(1,55), end=" ")
# #
# #
# # for i in range(10):
# #     print(random())
# #
# # x="string"
# # n=len(x)-1
# # while n>=0:
# #     print(x[n], end="")
# #     n=n-1
# #
# # k="aryana"
# # p=k[::-1]
# # print(p)
# #
# # # s=input('enter the string'  ,)
# # # f=s.split()
# # # rev=[x[::-1]for x in f]
# # # k=''.join(rev)
# # # print(k)
# #
# # from operator import add
# # list1=[1,2,3]
# # list2=[3,4,5]
# # # l=[list1[x]+list2[x]for x in range(len(list1))]
# # # print(l)
# # l=list(map(add,list1,list2))
# # print(l)
# #
# #
# # # k=['indra','jata']
# # # y=[x.upper()for x in k]
# # # print(y)
# #
# # list=["pen", "gun", "bun"]
# # upper=[x.title() for x in list]
# # print(upper)
# #
# # l1=[1,2,3]
# # l2=[4,5,6]
# # di={l1[x]:l2[x]for x in range(len(l1))}
# # print(di)
# #
# #
# # # fibonacci series
# # def fibb():
# #     a,b=0,1
# #     while True:
# #         yield(a)
# #         a,b=b,a+b
# # for f in fibb():
# #     if f>100:
# #         break
# #     print(f)
# #
# #
# # def factorial(n):
# #     if n==0:
# #         result=1
# #     else:
# #         result=n*factorial(n-1)
# #     return result
# # print(factorial(3))
# #
# # def fun(l):
# #      for x in l:
# #        if (x % 2)==0:
# #          print(x)
# # l=[1,2,3,4,5,6,7]
# # fun(l)
# #
# #
# # # palindrome series
# #
# # def palindrome(c):
# #     rev=(c)[::-1]
# #     if c==rev:
# #         return True
# #     else:
# #         return False
# # print(palindrome("madam"))
# #
# #
# # l="madam"
# # w=""
# # for x in l:
# #     w=x+l
# # if (l==w):
# #       print("yes")
# # else:
# #       print("false")
# #
# #
# #
# #
# #
# # # Python program to check
# # # if a string is palindrome
# #
# #
# #
# # k=["anitha", "kumar"]
# # p={x:k[x]for x in range(len(k))}
# # print(p)
# #
# # # list=["anitha", "kumar"]
# # # for x in list:
# # #     print(list)
# #
# # # palindrome number
# # # word=input("enter the word",)
# # # if (word==reversed(word)):
# # #        print("it is a palindrome")
# # # else:
# # #        print("not a palindrome")
# #
# # # string=input(("Enter a string:"))
# # # if(string==string.reverse()):
# # #       print("The string is a palindrome")
# # # else:
# # #       print("Not a palindrome")
# #
# # # import random
# # #
# # # randomlist = []
# # # for i in range(10):
# # #     n = random.randint(1, 30)
# # # randomlist.append(n)
# # # print(randomlist)
# #
# #
#
# # tuple=(1,2,3,4)
# import random
# l=[]
# for x in range(10):
#     n=random.randint(1,55)
#     l.append(n)
# print(l)
#
# def feb():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
#     # return a,b
#
# for i in feb():
#      if i>100:
#          break
#      print(i)
# # s="string"
# # print(s.rstrip("r"))
# # city=input("Enter your city Name:")
# # scity=city.strip()
# # if scity==' Hyderabad':
# #     print("Hello Hyderbadi..Adab")
# # elif scity=='  Chennai':
# #     print("Hello Madrasi...Vanakkam")
# # elif scity=="Bangalore":
# #      print("Hello Kannadiga...Shubhodaya")
# # else:
# #     print("your entered city is invalid")
#
#
#
# list1=[1,2,3]
# list2=[4,5,6]
# print(zip(list1,list2))
#
#
#
#
#
# num1=34
# def foo(num1):
#     num1=15
#     print(num1)
#     def bar(num1):
#      num1=44
#      print(num1)
#     return bar
# f1=foo(100)
# f1(77)
#
#
#
#
# # list1=[23,56]
# # list2=[55,77]
# # p=zip(list1,list2)
# # print(tuple(p))
#
# # from operator import add
# # list1=[23,56]
# # list2=[55,77]
# # l=[sum(i)for i in zip(list1,list2)]
# # print(l)
#
#
# # for i in range(5):
#
#
# # s = 'charan teja'
# # k=s.split(' ')
# #
# # l=[x[::-1]for x in k]
# # if x[0]==
# # n=' '.join(l)
# # print(n)
#
# s= 'Charan Teja in the air or rain'
# a = s.split(' ')
# x =a[0]
# n = len(x)-1
# w = ''
# for i in range(n,-1,-1):
#     w += x[i]
# print(w+" "+s[7:])
#
#
#
# # palindrome series for number
#
# # n=int(input("enter some num = ",))
# # rev=0
# # while n>0:
# #     dig=n%10
# #     rev=rev*10+dig
# #     num=n//10
# # if rev==n:
# #     print("the num is palindrome")
# # else:
# #     print("the num is not palindrome")
#
#
# list1 = [10, 20, 4,  46,44,66]
# list1.sort()
# print(list1)
# print("Largest element is:", list1[-1])
#
#
# # p=[3,4,5,6,7]
# # print(p)
#
#
#
def func(list):
    x=list[0]
    for i in list:
        if i>x:
            x=i
    print(x)

list=[2,3,6,7]
func(list)
#
# def func(list2):
#     list2.sort()
#     print("the  sec max number", list2[-2])
# list2=[33,44,55,66]
# # func(list2)
#
# # from operator import add
# p1=[1,2,3]
# p2=[4,5,6]
# l=[sum(x) for x in zip(p1,p2)]
# # print(l)
#
#
#
#
# # x="Welcome to India. india awesome, isn't it?"
# # o/p=? you are how hi
# str="Hi how are you ?"
# m=" "
# s=str.split()
# for x in s:
#     k=s[::-1]
#     m=''.join(k)
# print(m+ " " + x)
#
#
#
# x="India is a big country, I love india"
# # print(x.count("india"))
# y=x.lower()
# # print(y.count("india"))
#
#
# # def remove_adjacent_duplicates(s):
# #     chars = list(s)
# #     temp = ""
# #     k = 0
# #     for c in s:
# #         if temp != c:
# #             chars[k] = c
# #             temp = c
# #             k += 1
# #     return ''.join(chars[:k])
# # print(remove_adjacent_duplicates("acaaabbbbbbbacddddddddd"))
#
# # l=[]
# # s="acaaabbbbbbbacddddddddd"
# # i=0
# # while i<len(s):
# #     if i>=1:
# #         if s[i]==s[i-1] or s[i]==s[i+1]:
# #             continue
# #             i+=1
# #         else:
# #             l.append(s[i])
# #             i+=1
# #     else:
# #         l.append(s[i])
# #         i+=1
# # print(l)
#
#
# # def removeDuplicates(s):
# #     chars = list(s)
# #     prev = None
# #     k = 0
# #
# #     for c in s:
# #         if prev != c:
# #             chars[k] = c
# #             prev = c
# #             k = k + 1
# #     return ''.join(chars[:k])
# #
# #
# # if __name__ == '__main__':
# #     s = "AAABBCDDD"
# #
# #     s = removeDuplicates(s)
# #     print(s)
#
# #
# #
# #
#
#
def fun(l):
     x=l[0]
     for i in l:
         if i>x:
             x=i
     return x
l=[88,99,100]
print(fun(l))
#
#
# # lambda func
# s=lambda x:x+x
# print(s(5))
#
#
#
#
#
#
# # p='Hi how are you'
# # s=p.split()
# # t=s[0][::-1]
# # s[0] = t
# # res =""
# # for i in s:
# #     res +=' '+ i
# # print(res)
#
#
#
# # t="hello world"
# # s=t.split()
# # print(s)
# # o=s[0][::-1]
# # s[0]=o
# # print(s)
# # k=""
# # for i in s:
# #     k=k+ " "+i
# # print(k)

# i/p="Knowledge is devine"
# o/p="

pr="I am very happy ?"
t=pr.split()
print(t)
s=""
k= t[::-1]
# print(k)
s=' '.join(k)
print(s)


# i/p=Hello how are you
# o/p=olleh how are you

# s=input("enter the string", )
# w=s.split()
# print(w)
# k=w[1][::-1]
# print(k)
# w[1]=k
# print(w)
# ch=""
# for x in w:
#     ch=ch+" "+x
# print(ch)


# interchange first and last element in a list
l1=[1,2,3,45,6]
l1[0],l1[-1]=l1[-1],l1[0]
print(l1)



num=int(input("enter the number"))
if  num >1:
 for i in range(2,num):
    if (num%i)==0:
        print(num, "is a prime number")
        break

    else:
        print(num,"is not prime number")
else:
    print(num,"is not prime number")
# #
#
#
# # num = int(input("Enter a number: "))
# #
# # if num > 1:
# #     for i in range(2, num):
# #         if (num % i) == 0:
# #             print(num, "is not a prime number")
# #             # print(i, "times", num // i, "is", num)
# #             break
# #     else:
# #         print(num, "is a prime number")
# #
# # # else:
# # #     print(num, "is not a prime number")
#
#
#
#
#
# k="hello charan hi ?"
# d=k.split()
# print(d)
# s=""
# j=d[0][::-1]
# d[0]=j
# # print(d)
# for x in d:
#     s=s+" "+x
# # print(s)


# def even():
#     for i in range(0, 11, 2):
#         return i




# n=input("enter the string =",)
# i=len(n)-1
# while i>=0:
#     print(n[i], end="")
#     i=i-1
# print()







d={1:2, 3:2,4:5}
dict={val:key for key, val in d.items()}
# v={key:val for val, key in dict.items()}
print(dict)

list=[1,2,3,4,5,6,7,8,9,10]
for x in list:
    if x%2==0:
         print(x)

t=[1,2,3,4,5,6,7,8,9,10]
l=[x for x in t if x%2==0]
print(l)

l1=[1,2,3]
l2=[5,6,7]
y=[sum(i)for i in zip(l1,l2)]
print(y)

# highest method
l=[4,5,7,8,9]
x=l[0]
for i in l:
    if i>x:
        x=i
print(x)


k="students are good"
f=k.split()
print(f)
p=f[0][::-1]
# print(p)
f[0]=p
print(f)
s=""
for x in f:
    s=s+" "+x
print(s)



# removing duplicate values in dict
# dict={1:2, 3:2, 5:6}
# d={}
# temp=[]
# for key,value in dict.items():
#     if  value not in temp:
#         temp.append(value)
#         d[key]=value
# print(d)




k=["anitha", "kumar"]
p={x:k[x]for x in range(len(k))}
print(p)


d={1: 'charan', 2: 'kiran', 3:'charan'}
dict={value:key for key,value in d.items()}
k={key:value for value,key in dict.items()}
print(k)


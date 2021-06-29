def decorator(fun):
    def inner(a,b):
        if b==0:
            print('sorry 0 is not divisible')
        else:
            fun(a,b)
    return inner
@decorator
def div(a,b):
    return(a/b)
print(div(3,8))



def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')
print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)


def sum(*n):
   i=0
   for x in n:
       i=i+x
   return i
print(sum(4,5))

# s1=[2,3,4]
#
# p=[sum x for x in range(0,len(s1))]
# print(p)

# list=[2,3,4,5]
# f=[ for x in range(len(list))]
# print(f)


n=5
for x in range(0,n):
    for y in range(0,x+1):
        print(x,end=' ')
    print()



string = 'geeks'
length = 17

# If no fill character is provided, space
# is used as fill character
print(string.rjust(length))



l = [1, 0, 2, 6, 4, 0, 8, 0]
for x in range(len(l)):
    for y in range(x+1,len(l)):
        if l[x]>l[y]:
            l[x],l[y]=l[y],l[x]
print(l)

# o/p=[0,0,0,1,2,6,4,8]


# lst1 = []
# lst2 = []
# for x in l:
#     if x == 0:
#         lst1.append(x)
#     else:
#         lst2.append(x)
#
# new_lst = lst1 + lst2
# print(new_lst)




a = 'This is a sample program for evaluation'
k=a.split()
print(k)
d={x:len(x)for x in k}
print(d)
for k, v in d.items():
    if v%2==0:
        print(k,'has even',v)
    else:
        print(k,'has odd',v)





a = 'ARMY'
b = 'MARY'
print(a==b)

def cbv(x):
    x=45
    print(x)
x=34
cbv(34)
print(x)


def cbr(x):
    x[1]=34
    print(x)
l=[1,2,3]
cbr(l)
print(l)

n=[0,1,2,3,4,5,6]
for x in range(0,len(n)):
    for y in range(0,x+1):
        print('*',end=' ')
    print()



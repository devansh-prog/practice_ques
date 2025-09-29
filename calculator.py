# a=[1,2,3,4,5]
# print(list(map(lambda x:x**2,a)))
# a=lambda x,y:x+y
# print("sumis",a(10,20))
# a=[1,2,3,4,5]
# print(list(filter(lambda x:x%2==0,a)))
# import copy
# s=["hello","bye","goodmorning"]
# x=sorted(s,key=lambda x:x[-1])
# y=sorted(s,key=lambda x:x[0])
# print(True if x==y else False)

# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         if s[i][-1]>s[j][-1]:
#             s[i],s[j]=s[j],s[i]
# a=copy.deepcopy(s)
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         if s[i][0]>s[j][0]:
#             s[i],s[j]=s[j],s[i]
# x=copy.deepcopy(s)
# print(x,a)
# print(True if x==a else False)

# a=lambda x,y:x+y
# print(f"sum of numers are ",a(10,20))   
# b=lambda x:x%2==0
# print(b(2))
# square=lambda x:x**2
# print(square(5))
# words=["apple", "kiwi", "banana", "cherry"]
# # for word in words:
# #     l=sorted(words,key=lambda x:len(x))
# # print(l)
# l=sorted(words,key= lambda x:len(x))
# print(l)
# a=[1,2,3,4,5,6]
# print(list(map(lambda x:x**3,a)))
# print(list(filter(lambda x:x%2!=0,a)))

# a=[1,2,3,4,5]
k=2
# b=a[:k+1]
# a=a[k+1:]+b
# print(a)
# for i in range(k+1):
#     temp=a[0]
#     for j in range(1,len(a)):
#         a[j-1]=a[j]
#     a[len(a)-1]=temp
# print(a)

# a=[1,2,3,4,5]
# # a=[5,5,5,5,5]
# def l_e(a):
#     l=s=float('-inf')
#     for e in range(len(a)):
#         if a[e]>l:
#             s=l
#             l=a[e]
#         elif a[e]>s and a[e]!=l:
#             s=a[e]
#     return s if s != float('-inf') else None
# print("sec larget element is:",l_e(a))

# a=[1,2,3,4,5]
# t=7
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==t:
#             print(a[i],a[j])

# a=[1,2,1]
# b=a.copy()
# a.reverse()
# if a==b:
#     print(True)
# else:
#     print(False)
# x=[]
# for i in range(len(a)-1,-1,-1):
#     x.append(a[i])
# if a==x:
#     print(True)
# else:
#     print(False)


a=("A","B","D","D","D","B","B","C")
b=list(a)
# c=a.count(input("enter grade whose count u want:").upper())
# b.sort()
# print(c,b)
c={}
result=[]
for i in a:
    if i not in c:
        c[i]=1
    else:
        c[i]+=1

for key,val in c.items():
    result.extend([key]*val)
print(result)
# for key,val in c.items():
#     if key=="D":
#         print(val)
# b.sort()
# print(b)
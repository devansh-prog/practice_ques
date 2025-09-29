# s="[()]{}"
# a=[]
# for char in range(len(s)):
#     a.append(s[char])
# print(a)
# for i in range(len(a)):
#     if a[i]=="(":
#         print(i)
#         for j in range(i,len(a)):
#             if a[j]==")":
#                 print(j)
#                 a.pop(i)
#                 a.pop(j)
# print(a)
# while '()' in s or '[]' in s or '{}'in s:
#     s=s.replace('()','')
#     s=s.replace('[]','')
#     s=s.replace('{}','')
# if len(s)==0:
#     print("y")
# else:
#     print('n')
# for ch in range(len(s)):
#     a.append(s[ch])
# print(a)
# n=40
# m=30
# if m*n>1000:
#     a=m+n
# else:
#     a=n*m
# print(a)
n=10
t=0
p=0
sum=0
for i in range(n):
    temp=i
    sum=i+p
    p=temp
    
    print(i,p,sum)
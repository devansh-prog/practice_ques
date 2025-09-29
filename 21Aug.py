# a=[4,2,34,6,7,23,4,6,3,52,6,8,4,99,24,52]

# def l_e(a):
#     l=a[0]
#     s=a[0]
#     for e in range(1, len(a)):
#         if a[e] > l:  
#             s = l     
#             l = a[e]  
#         elif a[e] > s and a[e] != l:  
#             s = a[e]
#     return l, s
# l,s=l_e(a)
# print(l,s)

# v=len(a)
# def l_e(a):
#     l=a[0]
#     s=a[0]
#     for i in range(1,v):
#         if a[i]>l:
#             s=l
#             l=a[i]
#         elif a[i]>s and a[i]!=l:
#             s=a[i]
#     return l,s
        
# l,s=l_e(a)
# print(l,s)

# a=[1,2,3,4,5]
# for i in range(len(a)):
#     sqr=a[i]*a[i]
#     a[i]=sqr
# print(a)


# def l_e(a):
#     l=s=float('-inf')
#     for i in range(len(a)):
#         if a[i]>l:
#             s=l
#             l=a[i]
#         elif a[i]>s and a[i]!=l:
#             s=a[i]
            
#     return l,s if s!=float('-inf') else None

# a=[4,2,34,6,7,23,4,6,3,52,6,8,4,99,99,24,52,52,-10.-5]        
# l,s=l_e(a)
# print(l,s)

# def l_e(a):
#     l=s=float('-inf')
#     for i in range(len(a)):
#         if a[i]>l:
#             s=l
#             l=a[i]
#         elif a[i]>s and a[i]!=l:
#             s=a[i]
#     return l,s if s!=float('-inf') else None
# a=[4,2,34,6,7,23,4,6,3,52,6,8,4,99,99,24,52,52,-10.-5]    
# l,s=l_e(a)
# print

# s="3(ab)004(bcd)"   #abababbcdbcdbcdbcd  
# result=""
# i=0
# while i<len(s):
#     if s[i].isdigit():
#         num=0
#         while i<len(s) and s[i].isdigit():
#             num=num*10+int(s[i])
#             i+=1
#         if i<len(s)and s[i]=='(':
#             i+=1
#             temp=""
#             while i<len(s)and s[i]!=')':
#                 temp+=s[i]
#                 i+=1
#             i+=1
#             result+=temp*num
#         else:
#             result+=s[i]
#             i+=1
# print(result)
# a=[1,3,5,6,66,6,67,7,7,7,78,8,8,8,8,8,8]
# def del_dub(a):
#     unique=[]
#     for val in a:
#         if val not in unique:
#             unique.append(val)
#     return unique
    
# unique=del_dub(a)
# print(f"original array is {a}")
# print(f"unique elemements are{unique}")

# e=[]
# for val in a:
#     if val%2==0 and val not in e:
#         e.append(val)
# print(e)
# s=""
# for char in a:
#     s+=char
#     print(s)
# avg=s/len(a)
# print(f"avg is {avg}")
# print(s)

# a=[4,2,34,6,7,23,4,6,3,52,6,8,4,99,24,52]
# print(f"oriniginal list is {a}")
# unique=[]
# for val in a:
#     if val not in unique:
#         unique.append(val)
# print(f"unique list is {unique}")
# s=l=float('-inf')
# for e in unique:
#     if e>l:
#         s=l
#         l=e
#     elif e>s and e!=l:
#         s=e
# print(f"largest element of unique list is: {l} \nsecound largest element of unique list is: {s}")
# ev=(int(input("enter 1 to get even unique list- \n2 for odd-")))
# if ev==1:
#     even_unique=[]
#     for e in unique:
#         if e%2==0:
#             even_unique.append(e)
#     print(f"even unique list is- {even_unique}")
#     s=l=float('-inf')
#     for e in even_unique:
#         if e>l:
#             s=l
#             l=e
#         elif e>s and e!=l:
#             s=e
#     print(f"largest element of even unique list is: {l} \nsecound largest element of even unique list is: {s}")

# if ev==2:
#     odd_unique=[]
#     for e in unique:
#         if e%2!=0:
#             odd_unique.append(e)
#     print(f"odd list is- {odd_unique}")
#     s=l=float('-inf')
#     for e in odd_unique:
#         if e>l:
#             s=l
#             l=e
#         elif e>s and e!=l:
#             s=e
#     print(f"largest element of even unique list is: {l} \nsecound largest element of even unique list is: {s}")
# d={
# 	"a":12121,
# 	"b":123,
# 	"c":12345
# }

# nd={}
# for k,v in d.items():
#     if k=="b":
#         nd["B"]=v
#     else:
#         nd[k]=v 
# print(nd)

# a=[1,2,3,4,5]
# for i in range(len(a)):
#     sqr=a[i]*a[i]
#     a[i]=sqr
# print(a)
# a=[[1,2],[1,2,3],[4,5],[5,[6,7]]]
# b=[]
# for s in a:
#     for item in s:
#         b.append(item)
# print(b)
# a=[4,2,34,6,7,23,4,6,3,52,6,8,4,99,24,52]
# def l_e(a):
#     l=s=float('-inf')
#     for e in range(len(a)):
#         if a[e]>l:
#             s=lcls
#             l=a[e]
#     return l,s if s!=float('-inf') else None
# l,s=l_e(a)
# print(l,s)

 

# a=[[1,2,[1,2,3]],[4,[5]],[5,[6,[[[[[[7]]]]]]]]]

# for sublist in a:
#     # a=sublist[::-1]
#     for item in sublist:
#         if isinstance(item,list):
#             for inn in item:
#                 b.append(inn)
#         else:
#             b.append(item)
        
# print(b)
# def n(a):
#     for sublist in a:
#         for item in sublist:
#             if isinstance(item,list):
#                 for inn in item:
#                     b.append(inn)
#             else:
#                 b.append(item)
#     return b
# b=n(a)
# print(b)

# Python program to flatten a nested list

# explicit function to flatten a
# nested list
# def n(a):
#     if (not(bool(a))):
#         return a
#     if isinstance(a[0],list):
#         return n(*a[:1])+n(a[1:])
#     return a[:1]+n(a[1:])
# print(a)
# print(n(a))

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# def even(c,n):
#     if c>n:
#         return 
#     print(c)
#     even(c+2,n)
# even(2,20)

# def check_even(n):
#     if n==0:
#         return print("even")
#     elif n==1:
#         return print("odd")
#     elif n<0:
#         return check_even(abs(n))
#     else:
#         return check_even(n-2)
# check_even(7)

# def check_plaindorme(s):
#     if s=="":
#         return print("empty")
#     else:
#         temp=s
#         if temp[::-1]==s:
#             print("palindorme")
#         else :
#             print("not palindrome")
# s="madam"        
# check_plaindorme(s)

# def print_num(s,n):
#     if s>n:
#         return 
#     print(s)
#     print_num(s+1,n)
# print_num(1,10)

# def sum_n(s,n,sum=0):
#     if s>n:
#         return
#     sum+=s
#     print(sum)
#     sum_n(s+1,n,sum)
    
# sum_n(1,10)
# def max_ele(a,c=0):
#     if (not(bool(a))):
#         return a
#     x=[]
#     for i in range(1,len(a)):
#         if a[i]!=x[i]:
#             x.append(a[i])
#             c+=1
#     return c
# a=[1,2,1,2,3,3,4,5,6,6,6,6]    
# c=max_ele(a)
# print(c)
# value="hello"
# s=""
# for ind in range(len(value)-1,-1,-1):
#     s+=value[ind]
# print(s)
# value="hello"
# s=""
# for ch in value:
#     s=ch+s
# print(s)

# s="devansh"
# x={'a','e','i','o','u'}
# count=0

# for ch in s:
#     for v in x:
#         if ch==v:
#             count+=1
# print(count)



 

# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# print(fact(4))

# def Sum(s,n,total=0):
#     if s>n:
#         return
#     total+=s
#     print(total)
#     Sum(s+1,n,total)
    
# Sum(1,10)
# def Sum(n):
#     if n==1:
#         return 1
#     return n+Sum(n-1)
# print(Sum(5))


# def even(c,n):
#     if c>n:
#         return 
#     print(c)
#     even(c+2,n)
# even(2,20)
        
# a=[1,2,3,2,4,3,5,6,7,5,7,8,9,8]

# def max_e(a):
#     if len(a)==1:
#         return a[0]
#     largest=max_e(a[1:])
#     return a[0] if a[0]>largest else largest

# print(max_e(a)) 

# a=[1,2,3,4]
# def sum_l(a):
#     sum=0
#     if len(a)==1:
#         return a[0]
#     sum+=a[0]+sum_l(a[1:])
#     return sum
# print(sum_l(a))

# a=[[1,2,[1,2,3]],[4,[5]],[5,[6,[[[[[[7]]]]]]]]]
# def n(a):
#     if (not(bool(a))):
#         return a
#     if isinstance(a[0],list):
#         return n(*a[:1])+n(a[1:])
#     return a[:1]+n(a[1:])
# print(a)
# print(n(a))

# def n(a):
#     if (not (bool(a))):
#         return a
#     if isinstance (a[0],list):
#         return n(*a[:1])+n(a[1:])
#     return a[:1]+n(a[1:])
# print(n(a))

# a=[0,2,3,4,5000]
# l=float('-inf')
# s=float('inf')
# for i in range(len(a)):
#     if a[i]>l:
#         l=a[i]
#     if a[i]<s:
#         s=a[i]
# print(f"largest {l},smallest ele {s}")

# a=[8,7,6,7,8]
# b=0
# for i in range(len(a)):
#     b+=a[i]
# print("sum of elemnets are:"b)

# a=[1,2,3,4,4,5,5,57,7,7,0]
# c=0
# for num in range(len(a)):
#     if a[num]%2==0:
#         c+=1
# print(c)
# odd=len(a)-c
# print(odd)

# a=[1,2,3,4,4,5,5,57,7,7,0]

# for i in range(len(a)-1,-1,-1):
#     print(a[i],end=" ")
# a=[1,2,3,4,4,5,5,57,7,7,0]
# rev=[]
# for i in range(len(a)-1,-1,-1):
#     rev.append(a[i])
# print(rev)
# a=[1,2,3,4,4,5,5,57,7,7,0]
# for i in range(len(a)//2):
#     a[i],a[len(a)-1-i]=a[len(a)-1-i],a[i]
# print(a)

# a=[1,2,3,4,4,5,5,57,7,7,0]
# n=int(input("enter ele u wnat to find: "))
# for i in range(len(a)):
#     if a[i]==n:
#         print(f"element {n},index is {i}")
# else:
#     if n not in a:
#         print("Element not found")
# a=[1,2,3,3,4,5,4,3,66,6,8,8]
# d=[]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]==a[j] and a[i] not in d:
#             d.append(a[i])
# print(d)

# a=[1,2,3,3,4,5,4,3,66,6,8,8]
# a=[4,2,34,6,7,23,4,6,3,52,6,8,4,99,24,52]
# def sec(a):
#     l=s=float('-inf')
#     for e in a:
#         if e>l:
#             s=l
#             l=e
#         elif e>s and e!=l:
#             s=e
#     return s
# ans=sec(a)
# print(ans)
# a=[4,2,34,6,7,23,4,6,3,52,6,8,4,99,24,52]
# for n in range(len(a)-1,0,-1):
#     for i in range(n):
#         if a[i]>a[i+1]:
#             a[i],a[i+1]=a[i+1],a[i]
# print("acending:",a)
# print("decending",a[::-1])

# a=[4,2,34,6,7,23,4,6,3,52,6,8,4,99,24,52]
# k=3
# l=[]
# for i in range(k+1):
#     l.append(a[0])
#     a.pop(0)
# print(l)
# print(a)
# print(a+l)
# a=[1,0,0,0,6,0]
# n=len(a)
# l=[0]*(n-2)
# for i in range(n):
#     if a[i]!=0:
#         l.append(a[i])
# x=n-len(l)
        
# print(l)
# print(a)
s="smurti"
# for i in range(len(s)):
#     print(s[i]+"."+s[i],end="")


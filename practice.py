# #a=[1,2,3,4,5,6,7,88,0] output[88,7] lrgest and sec largest
# # def l_e(a):
# #     l=a[0]
# #     s=a[0]
# #     for e in range(1, len(a)):
# #         if a[e] > l:  
# #             s = l     
# #             l = a[e]  
# #         elif a[e] > s and a[e] != l:  
# #             s = a[e]
# #     # print(s)
# #     return l, s
    
# # a=list(map(int,input('enter the values of array with :').split(',')))
# # print(a)
# # # a=[0,0,0]
# # largest, second_largest = l_e(a)
# # print(f"largest element is:{largest}, seclargest{ second_largest}")

# # value="hello"
# # s=""
# # for ch in value:
# #     s=ch+s
# # print(s)

# # s="devansh"
# # x={'a','e','i','o','u'}
# # count=0

# # for ch in s:
# #     for v in x:
# #         if ch==v:
# #             count+=1
# # print(count)

# # s="hello world"
# # rev=[]
# # for i in range(len(s)-1,-1,-1):
# #     rev.append(s[i])
# # revs=""
# # for ch in rev:
# #     revs+=ch
# # print(revs)

# # s="devnash"
# # rev=[]
# # for i in range(len(s)-1,-1,-1):
# #     rev.append(s[i])
# # revs=[]
# # for ch in rev:
# #     revs+=ch
# # print(revs)
# # 
# #reverse a string
# # s="hello"
# # rev=""
# # for ch in s:
# #     rev=ch+rev
# # print(rev)

# #reverse string and elements too
# # s="hello bye eve"
# # l=len(s)
# # a=""
# # for ch in range(l):
# #     a=s[ch]+a
# # print(a)

# #reverse the string elements
# # s="hello bye eve"
# # words=[]
# # word=""
# # c=0

# # for ch in s:
# #     if ch != " ":
# #         word += ch
# #     else:
# #         words.append(word)
# #         word = ""

# # words.append(word)

# # for i in range(len(words)-1,-1,-1):
# #     print(words[i],end=" ")

# a=[0,1,2,2,3,0,4,2]
# def remove(a):
#     l1=len(a)
#     b=set(a)
#     b=list(b)
#     l2=len(b)
#     ans=l1-l2
#     newarr=b+["_"]*ans
#     return newarr

# ans=remove(a)
# print(ans)


# #reverse a string
# # s="hello"
# # rev=""
# # for ch in s:
# #     rev=ch+rev
# # print(rev)

# # reverse string and elements too
# # s="hello bye eve"
# # l=len(s)
# # a=""
# # for ch in range(l):
# #     a=s[ch]+a
# # print(a)

# #reverse the string elements

# # s="hello bye eve"
# # words=[]
# # word=""

# # for ch in s:
# #     if ch != " ":
# #         word += ch
# #     else:
# #         words.append(word)
# #         word = ""

# # words.append(word)

# # for i in range(len(words)-1,-1,-1):
# #     print(words[i],end=" ")

# s='apple'
# result=""
# for i in range(len(s)):
#     count=0
#     for j in range(len(result)):
#         if s[i]==result[j]:
#             count=1
#             break
#     if count==0:
#         result=result +s[i]
# print(result)

# # n=121
# # temp=temp2=n
# # rev=0

# # while temp>0:
# #         r=temp%10
# #         rev=rev*10+r
# #         temp//=10
# # if rev==n:
# #     print("palamdrone")
# # else:
# #     print("not")'

# # n = 23
# # seen = []
# # while n != 1 and n not in seen:
    
# #     seen.append(n)    
# #     s = 0
# #     temp = n
# #     while temp > 0:
# #         r = temp % 10    
# #         s = s + r**2     
# #         temp = temp // 10  
# #     n = s 
# #     print(f"Next number: {n}")
    
# # if n == 1:
# #     print("Happy Number! 🎉")
# # else:
# #     print("Not a happy number (cycle found)")







# # n = 100  # Change this to any limit you want

# # print(f"Happy numbers up to {n}:")

# # # Check each number from 1 to n
# # for i in range(1, n + 1):
    
# #     # Test if current number i is happy
# #     num = i
    
#     # Keep calculating until we reach 1 or 4
#     # (4 means it will cycle and never reach 1)
# #     while num != 1 and num != 4:
        
# #         # Calculate sum of squares of digits
# #         s = 0
# #         temp = num
# #         while temp > 0:
# #             digit = temp % 10    # Get last digit
# #             s = s + digit * digit  # Add square of digit
# #             temp = temp // 10    # Remove last digit
        
# #         num = s  # Update num with sum
    
# #     # If we reached 1, it's a happy number
# #     if num == 1:
# #         print(i, end=' ')

# # print()


# # a={
# # 	"a":12121,
# # 	"b":123,
# # 	"c":12345
# # }
# # # output={"a":12121,
# # # 	"B":123,
# # # 	"c":12345}
# # a=[1,2,3,4,5] 
# # for i in range(len(a)):
# #     s=a[i]*a[i]
# #     a[i]=s
# # print(a)

# #print arry elements 
# # a=['a','b','c','d']    
# # s=""
# # for char in a:
# #     s+=char
# # print(s)

# #remove dublicate
# # a=[1,2,3,4,5,6,7,8,9,9,3,2,1,2]
# # a=['a','b','c','c','d','d','a']
# # a=[0,0,0,0,0,0,4]
# # a=[-1,-2,-5,-5,-1,-3,-4]
# # unique=[]
# # for val in a:
# #     if val not in unique:
# #         unique.append(val)
# # print(unique)
# #remove even
# # unique=[]
# # for val in a:
# #     if val%2==0 and val not in unique:
# #         unique.append(val)
# #         print(val)

# # a=[4,2,34,6,7,23,4,6,3,52,6,8,4,99,24,52]
# # def l(a):
# #     l=s=float('-inf')
# #     for e in range(len(a)):
# #         if a[e]>l:
# #             l=a[e]
# #         elif a[e]>s and a[e]!=l:
# #             s=a[e]
# #     return l,s
# # l,s=l(a)
# # print(f"largest element is {l} and secound largest element is {s}")

# # a=[4,2,34,6,7,23,4,6,3,52,6,8,4,99,24,52]
# # print(f"original list :{a}")
# # unique=[]
# # l=s=float('-inf')
# # for val in a:
# #     if val not in unique:
# #         unique.append(val)
# # print(f"unique list is {unique}")
# # l=s=float('-inf')
# # for e in unique:
# #     if e>l:
# #         s=l
# #         l=e
# #     elif e>s and e!=l:
# #         s=e       
# # print(f"largest element of a unique list {l},secound largest element of unique list is {s}")

# d={
# 	"a":12121,
# 	"b":123,
# 	"c":12345
# }
# new_d={}
# for k,v in d.items():
#     if k=="b":
#         new_d["B"]=v
#     else:
#         new_d[k]=v
# print(new_d)

# # a=[4,2,34,6,7,23,4,6,3,52,6,8,4,99,24,52]
# # unique=[]
# # for val in a:
# #     if val not in unique:
# #         unique.append(val)        
# # print(unique)
# # def l_e(unique):
# #     l=s=float('-inf')
# #     for e in a:
# #         if e>l:
# #             s=l
# #             l=e
# #         elif e>s and e!=l:
# #             s=e
# #     return l,s 
# # l,s=l_e(unique)
# # print(f"largest elemment in unique list is {l}\nScound largest element in unique list is {s}")

# # a=[[1,2],[1,2,3],[4,5],[5,[6,7]]]
# # b=[]
# # for sublist in a:
# #     for item in sublist:
# #         if isinstance(item,list):
# #             for innet_item in item:
# #                 b.append(innet_item)
# #         else:
# #             b.append(item)
# # for i in range(len(b)):
# #     if b[i]==7:
# #         print(f"found entered element {b[i]} its position is {i}")
# # print(b)

# # a=[3,4,7,99,100,1,0]
# # min=a[0]

# # for i in range (1,len(a)):
# # 	if a[i]<min:
# # 		min=a[i]

# # a=[1,3,4,5,6,7,3,4,5,6,7,89,89,90,90,12,23,90]
# # s=[]
# # for i in range(len(a)):
# #     for j in (i+1,len(a)+1):
# #         temp=a[i:j]
# #         if temp.count(max_val)>=3:
# #             s.append(a[i:j])
# # print(s)
# # m=max(s)
# # print(m,"max")

# # a = [1,3,4,5,6,7,90,3,4,5,6,7,89,89,90,90,12,23,90]
# # # a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# # max_val=max(a)
# # need = a.count(max_val) 
# # print(max_val,"max val")
# # n=len(a)
# # sub=[]
# # for i in range(n):    
# #     for j in range(i+1,n+1):
# #         if a[i:j].count(max_val)==need:
# #             sub.append(a[i:j])
# # print("sortest sub sublist ",sub[-1])


# # a = [1,3,4,5,6,7,3,4,5,6,7,89,89,90,90,12,23,90]

# # max_val = max(a)  
# # n = len(a)
# # max_count = 0
# # result = []

# # for i in range(n):
# #     for j in range(i+1, n+1):
# #         sub = a[i:j]
# #         if max_val in sub:
# #             count = sub.count(max_val)
# #             if count > max_count:
# #                 max_count = count
# #                 result = [sub]
# #             elif count == max_count:
# #                 result.append(sub)

# # print("Largest element:", max_val)
# # for sub in result:
# #     print(sub)

# def find_shortest_subarray_optimal(a):
#     if not a:
#         return []
    
#     max_val = max(a)
    
#     # Find all positions of max_val
#     positions = []
#     for i in range(len(a)):
#         if a[i] == max_val:
#             positions.append(i)
    
#     if not positions:
#         return []
    
#     # The shortest subarray containing all max values
#     # goes from first occurrence to last occurrence
#     print(positions)
#     start = positions[0]
#     end = positions[-1]
    
#     return a[start:end+1]

# a = [1,3,4,5,6,7,90,3,4,5,6,7,89,89,90,90,12,23,90]
# print(find_shortest_subarray_optimal(a))

# a=25
# b=30
# temp=a
# a=b
# b=temp
# print(a,b)

# x=2
# y=7
# x=x+y
# y=x-y
# x=x-y
# print(x,y)
# a=10
# b=20
# c=30
# a,b,c=c,b,a
# print(a,b,c)
# a=[10,30]

# s="3(ab)004(bcd)"#output abababbcdbcdbcdbcd
# result=""
# i=0
# while i<len(s):
#     if s[i].isdigit():
#         num=0
#         while i<len(s) and s[i].isdigit():
#             num=num*10+int(s[i])
#             i+=1
#         if s[i]=="(":
#             i+=1
#             temp=""
#             while i<len(s)and s[i]!=')':
#                 temp+=s[i]
#                 i+=1
#             i+=1
#             result=temp*num
#         else:
#             result+=s[i]
#             i+=1
# print(result)
    
# s="3(ab)004(bcd)"   #abababbcdbcdbcdbcd  
# result=""
# i=0
# while i<len(s):
#     if s[i].isdigit():
#         num=0
#         while i<len(s) and s[i].isdigit():
#             num=num*10+int(s[i])
#             i+=1
#         if s[i]=="(":
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
# a=[1,2,3,4,5,6,7,8,8,9,0,1,2,3,5,5,5,5]
# unique=[]
# for val in a:
#     if val not in unique:
#         unique.append(val)
# print(unique)

# a=[4,2,34,6,7,23,4,6,3,52,6,8,4,99,24,52]
# def l_e(a):
#     l=s=float('-inf')
#     for e in range(len(a)):
#         if a[e]>l:
#             s=l
#             l=a[e]
#         elif a[e]>s and a[e]!=l:
#             s=a[e]
#     return l,s
# l,s=l_e(a)
# print(l,s)

# a=[4,2,34,6,7,23,4,6,3,52,6,8,4,99,24,52]
# # unique=[]
# # for val in a:
# #     if val not in unique:
# #         unique.append(val)
# # print(unique)
# print(sorted(a,reverse=True))
# l=list(dict.fromkeys(a))
# print(l)


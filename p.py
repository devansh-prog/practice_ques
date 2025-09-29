# #purelogic
# a=[4,2,34,6,7,23,4,6,3,52,6,8,4,99,24,52,100,0]
# def l_e(a):
#     l=s=float('-inf')
#     for e in range(len(a)):
#         if a[e]>l:
#             s=l
#             l=a[e]
#         elif a[e]>s and a[e]!=l:
#             s=a[e]
#     return(l,s)
# l,s=l_e(a)
# print(l,s)
# #inbuild method 
# a=[4,2,34,6,7,23,4,6,3,52,6,8,4,99,24,52,100,0]
# s=sorted(a)
# print(s[-2],s[-1])
# a=[4,2,34,6,7,23,4,6,3,52,6,8,4,99,24,52,100,0]
# s=[]
# s.append(max(a))
# print(s)
# a.remove(max(a))
# s.append(max(a))
# print(s)
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
s="abc"
l=list(s) 
e=input("enter element u wnat to replave:")
for val in l:
    if val==e:
        print("j")
    else:
        print("k")
m=input("enter repaced val:")

    
# print(l)



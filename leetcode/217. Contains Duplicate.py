# a=[1,0,1,1]
# k=1
# found=False
# for i in range (len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]==a[j]and abs(i-j)<=k:
#             print(True)
#             found=True
#             break
#     if found:
#         break
# if not found:
#     print(False)
a=[1,0,1,1]
k=1
seen={}
for i,val in enumerate(a):
    if val in seen and i - seen[val]<=k:
        print(True)
        break
    seen[val]=i
print(False)
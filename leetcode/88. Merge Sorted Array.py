
a=[-1,0,0,3,3,3,0,0,0]
b=[1,2,2]
m=6
n=3
i=m-1
j=n-1
k=m+n-1
while j>=0:
    if i >=0 and a[i]>b[j]:
         a[k] = a[i]
         i -= 1
    else:
        a[k] = b[j]
        j -= 1
    k -= 1

print(a)
    
        

# l1 = [9,9,9]
# l2 = [9,9,9]
l1 = [5,5,4,4,1]
l2 = [6,7,2,9,5]
n=len(l1)
s=0
l=[]
r=0
for i in range(n-1,-1,-1):
    s=l1[i]+l2[i]+r
    r=s//10
    s=s%10
    l.append(s)
        
l.reverse()

print([r]+l)
# print(r)

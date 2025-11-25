l=[1,2,3,5,6,7,8,88,99,19,66,54,70]
e=[x for x in l if x%2==0]
o=[x for x in l if x%2!=0]

max_x=max(len(e),len(o))
r=[]
i=0
while i <max_x:
    if i<len(o):
        r.append(sum(o[i:i+2]))
    if i<len(e):
        r.append(sum(e[i:i+2]))
        
    i+=2
print(r)
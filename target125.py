l=[1,2,3,5,6,7,8,88,99,19,66,55,70]
t=125

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==t:
            print(i,j)
        


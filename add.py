# n=int(input("enter number 1: "))
# m=int(input("enter number 1: "))
# print(n,m)
def add(n,m):
    while m!=0:
        s=m^n
        c=(m&n)<<1
        n=s
        m=c
    return n
n=int(input("enter number 1: "))
m=int(input("enter number 2: "))
ans=add(n,m)
print(ans)

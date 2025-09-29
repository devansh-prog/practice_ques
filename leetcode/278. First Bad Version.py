
def isBadVersion(v):
    bad=7
    if v>=bad:
        return True
    else:
        return False
def firstBadVersion(n):
    l,r=1,n
    while l<r:
        mid=l+(r-l)//2
        if isBadVersion(mid):
            r=mid
        else:
            l=mid+1
    return l
n=int(input("enter value of n:"))
ans=firstBadVersion(n)
print(ans)
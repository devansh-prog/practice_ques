s1="listen"
s2="silent"
# f=True
#way1:inbuild functions
# if sorted(s1)==sorted(s2):
#     print(True)
# else:
#     print(False)

#way2:Pureloop
# if len(s1)!=len(s2):
#     f=False

# for ch in s1:
#     if ch in s2:
#         continue
#     else:
#         f=False
#         break
# print(f)

#way3:
def c(s1,s2):
    if len(s1)!=len(s2):
        return False
    f1={}
    f2={}
    
    for ch in s1:
        if ch in f1:
            f1[ch]+=1
        else:
            f1[ch]=1
    for ch in s2:
        if ch in f2:
            f2[ch]+=1
        else:
            f2[ch]=1
    return f1==f2
print(c(s1,s2))



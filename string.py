s="hello"
n=int(input("enter the value : "))
if 0<=n<len(s):
    for ch in range(n,len(s)):
        print(s[ch])
elif n==len(s):
    print("String emptyed out")
else:
    print("invalid")
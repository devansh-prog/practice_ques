n=int(input("enter the number:"))
rem=0
result=''
if n<0:
    print("give only +ve numbers ")
while n>0:
    n-=1
    rem=n%26
    result=chr(ord('A')+rem)+result
    n//=26
print("colum in exel sheet is ",result)
def con(s):
    x=0
    for ch in s:
        x = x * 26 + (ord(ch) - ord('A') + 1)
    print(f"decimal val  is {x}")
s=input("give string u wnat to covert to deximal:")
con(s)

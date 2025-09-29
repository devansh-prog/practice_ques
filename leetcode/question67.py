a="11"
b="1"
sum=bin(int(a,2)+int(b,2))
print(sum)
if sum.startswith("0b"):
    print(sum[2:])
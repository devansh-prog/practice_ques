# n=input("enter a number :")
# s=0
# if len(n)%2==0:
#     s=int(n[:2])+int(n[2:])
# print(s)
def sqrt_long_division(n):
    s = str(n)
    if len(s) % 2 == 1:
        s = "0" + s
    pairs = [int(s[i:i+2]) for i in range(0, len(s), 2)]

    result = 0
    remainder = 0

    for p in pairs:
        remainder = remainder * 100 + p
        x = 0
        candidate = 0
        while True:
            if (20 * result + (x+1)) * (x+1) <= remainder:
                x += 1
            else:
                break

        candidate = (20 * result + x) * x
        remainder -= candidate
        result = result * 10 + x

    return result

n=input("enter a number :")
print(sqrt_long_division(n)) 
#devansh
